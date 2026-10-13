# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class GrantEvaluator(gl.Contract):
    admin: Address
    proposal_count: u32
    evaluations: TreeMap[u32, str]

    def __init__(self):
        self.admin = gl.message.sender_address
        self.proposal_count = u32(0)

    @gl.public.write
    def submit_and_evaluate_proposal(
        self, 
        applicant_name: str, 
        project_title: str, 
        description: str, 
        requested_amount: u32
    ) -> str:
        self.proposal_count = u32(self.proposal_count + 1)
        current_id = self.proposal_count

        def run_llm_eval() -> str:
            prompt = f"""
            You are an objective DAO Grant Evaluation Committee consensus agent.
            Evaluate the following grant proposal strictly based on clarity, feasibility, and budget:

            Applicant: {applicant_name}
            Project: {project_title}
            Grant Requested: {requested_amount} tokens
            Description: {description}

            Rate the proposal and give a verdict: APPROVED, REVISION_NEEDED, or REJECTED.
            Return ONLY a single valid JSON string:
            {{"score": 85, "verdict": "APPROVED", "notes": "Solid technical plan."}}
            """
            return gl.nondet.exec_prompt(prompt)

        raw_result = gl.eq_principle.strict_eq(run_llm_eval)
        clean_result = raw_result.strip().replace("```json", "").replace("```", "")
        
        # Store in GenLayer persistent TreeMap
        self.evaluations[current_id] = clean_result

        return f"Proposal #{current_id} evaluated and recorded."

    @gl.public.view
    def get_evaluation(self, proposal_id: u32) -> str:
        return self.evaluations.get(proposal_id, "Proposal not found")

    @gl.public.view
    def get_total_proposals(self) -> u32:
        return self.proposal_count
