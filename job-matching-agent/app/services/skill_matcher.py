import re

SKILL_ALIASES = {
    "office 365": "microsoft 365",
    "o365": "microsoft 365",
    "m365": "microsoft 365",
    "microsoft office 365": "microsoft 365",
    "ms office": "microsoft office",
    "ms office suite": "microsoft office",
    "microsoft office suite": "microsoft office",
    "ms office applications": "microsoft office",
    "word": "microsoft word",
    "ms word": "microsoft word",
    "excel": "microsoft excel",
    "ms excel": "microsoft excel",
    "powerpoint": "microsoft powerpoint",
    "ms powerpoint": "microsoft powerpoint",
    "outlook": "microsoft outlook",
    "ms outlook": "microsoft outlook",
    "g suite": "google workspace",
    "google suite": "google workspace",
    "windows": "windows os",
    "ms windows os": "windows os",
    "windows 10": "windows 10/11",
    "windows 11": "windows 10/11",
    "mac os": "macos",
    "ticketing system": "ticketing",
    "ticketing systems": "ticketing",
    "helpdesk": "help desk",
    "service now": "servicenow",
    "postgres": "postgresql",
    "tsql": "t-sql",
    "microsoft sql server": "sql server",
    "ms sql": "sql server",
    "mssql": "sql server",
    "js": "javascript",
    "reactjs": "react",
    "react.js": "react",
    "nodejs": "node.js",
    "k8s": "kubernetes",
    "gcp": "google cloud",
    "red hat enterprise linux": "rhel",
    "s/4hana": "sap s/4hana",
    "sap s4hana": "sap s/4hana",
    "crm systems": "crm",
    "crm platforms": "crm",
    "crm software": "crm",
    "erp systems": "erp",
    "erp system": "erp",
    "pdu": "pdus",
    "sop": "sops",
    "root cause analysis": "rca",
    "multimeter": "multimeters",
    "oscilloscope": "oscilloscopes",
    "firewall": "firewalls",
    "vpns": "vpn",
    "vlan": "vlans",
    "powerbi": "power bi",
}


def normalize_skill(skill: str) -> str:

    skill = skill.lower().strip()

    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills: list[str]) -> set[str]:

    return {normalize_skill(skill) for skill in skills if skill.strip()}


def is_skill_covered(skill: str, profile_skills: set[str]) -> bool:
    """
    True when a normalized job skill is in the profile,
    either exactly or as a whole phrase inside a longer
    profile entry: "linux" is covered by "embedded linux",
    "dhcp" by "dns/dhcp", "customer service" by
    "customer service skills".
    """

    if skill in profile_skills:
        return True

    pattern = re.compile(r"(?<!\w)" + re.escape(skill) + r"(?!\w)")

    return any(pattern.search(profile_skill) for profile_skill in profile_skills)
