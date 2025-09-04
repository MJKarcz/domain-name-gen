# 🚀 Domain Name Generator with LLMs

## 📌 Project Overview
This project explores the use of **Large Language Models (LLMs)** to generate and iteratively improve **domain name suggestions**.  
The goal is to build a system that:
- Generates creative domain names
- Evaluates their quality using an LLM-as-a-judge framework
- Incorporates **safety guardrails** to avoid inappropriate suggestions
- Improves iteratively through feedback and fine-tuning

---

## 🧩 Components
1. **Domain Name Generation**
   - Base model: [Model Name & Size, e.g., `llama3.2:1b`]
   - Fine-tuning method: [LoRA / full fine-tuning / prompt-engineering]

2. **Evaluation (LLM-as-a-Judge)**
   - Criteria:
     - ✅ Relevance to the prompt
     - ✅ Creativity / brandability
     - ✅ Availability likelihood
     - ✅ Safety compliance
   - Judge model: [e.g., `phi3:3.8b`, external GPT-4]

3. **Safety Layer**
   - Keyword/regex filters
   - Optional: safety LLM (`llama-guard3`)

---

## 📊 Current Progress
- [x] Selected baseline model
- [x] Designed evaluation criteria
- [ ] Implemented generation pipeline
- [ ] Implemented evaluation pipeline
- [ ] Safety filtering
- [ ] Iterative feedback loop
- [ ] Documentation & final report

---

## 🔬 Experiments
### Baseline Generation
- **Model used:** [e.g., llama3.2:1b]
- **Prompt style:** [insert example]
- **Observations:**
  - [e.g., names are short but repetitive]
  - [e.g., creativity limited]

### Iterative Improvement
- Plan: [e.g., fine-tune with curated dataset of brandable names]
- Next steps: [e.g., evaluate with LLM-judge scoring]

---

## ⚠️ Limitations
- Small models (1B) struggle with creativity and safety
- Evaluation reliability depends on judge model quality
- True domain availability is not guaranteed without external checks

---

## 🛠️ Next Steps
- [ ] Collect dataset of good vs. bad domain names
- [ ] Fine-tune base model with LoRA
- [ ] Integrate evaluation loop
- [ ] Apply safety guardrails
- [ ] Write final report

---

## 📚 References
- [Meta Llama 3.1/3.2 Models](https://huggingface.co/meta-llama)
- [Ollama Model Library](https://ollama.com/library)
- [LoRA Fine-Tuning Guide](https://huggingface.co/docs/peft)

---

## 👤 Author
- Name: [Your Name]  
- Course: [Course Name]  
- Assignment: [Homework/Project Number]  
