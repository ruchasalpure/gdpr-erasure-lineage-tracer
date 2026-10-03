from crewai import Agent

gdpr_erasure_lineage_tracer = Agent(
    role="Gdpr Erasure Lineage Tracer",
    goal="Deliver high-precision autonomous Gdpr Erasure Lineage Tracer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
