from ollama import chat, RequestError, ResponseError


class AIMatchAgent:

    def __init__(self):
        # Set when Ollama can't be reached, so the
        # remaining jobs don't retry it one by one.
        self.unavailable_reason = None

    def analyze(
        self, job_title, company, job_skills, matched_skills, missing_skills
    ) -> str:

        explicit_skills = ", ".join(job_skills) if job_skills else "NONE"

        matched = ", ".join(matched_skills) if matched_skills else "NONE"

        missing = ", ".join(missing_skills) if missing_skills else "NONE"

        prompt = f"""
You are a strict job matching report generator.

Job Title:
{job_title}

Company:
{company}

Explicit Skills Extracted:
{explicit_skills}

Matched Skills:
{matched}

Missing Skills:
{missing}

Follow these rules exactly:

1. Never invent skills.

2. Explicit Skill Match must contain ONLY skills
   from Matched Skills.

3. Explicit Missing Skills must contain ONLY skills
   from Missing Skills.

4. Learning Recommendations must contain ONLY
   skills from Missing Skills.

5. NEVER recommend a matched skill.

6. If Missing Skills is NONE, Learning Recommendations
   must be NONE.

7. If Explicit Skills is NONE, say:
   "No explicit skills were extracted from the available job description."

8. Do not infer skills from the job title.

9. Do not infer skills from the company.

10. Do not change the provided match information.

Return exactly:

1. Explicit Skill Match
2. Explicit Missing Skills
3. Learning Recommendations
"""

        if self.unavailable_reason:
            return f"AI analysis unavailable: {self.unavailable_reason}"

        try:
            response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a strict reporting assistant. "
                            "Only use the exact information provided. "
                            "Never invent, infer, or recommend "
                            "a skill that is not explicitly present "
                            "in Missing Skills."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
            )

        except ConnectionError as error:
            self.unavailable_reason = str(error)
            return f"AI analysis unavailable: {error}"

        except (RequestError, ResponseError) as error:
            # e.g. the llama3.2 model is not pulled
            return f"AI analysis failed: {error}"

        return response["message"]["content"]
