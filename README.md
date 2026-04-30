# 📄 From Prompt to Vulnerability: Understanding Security Risks in AI-Generated Code

## 🔍 Introduction
AI-powered code generation tools such as GitHub Copilot, ChatGPT, and Amazon CodeWhisperer are transforming modern software development by improving productivity and reducing development time.

However, this convenience comes with a critical trade-off — **security**.

This research explores how AI-generated code can unintentionally introduce vulnerabilities into software systems. By analyzing multiple studies and real-world scenarios, we identify patterns, root causes, and risks associated with relying on AI for code generation.

📊 **Key Insight:**  
AI-generated code can be up to **1.8× more vulnerable** than human-written code, especially in security-sensitive applications.

---

## 📌 About the Research
This repository contains our research paper that:

- Identifies **11 categories of security vulnerabilities**
- Maps them to **MITRE CWE standards**
- Analyzes **why vulnerabilities occur in AI-generated code**
- Compares leading AI coding tools
- Suggests **practical mitigation strategies**

---

## 👩‍💻 Authors
- **Palak Kaushik**  
- **Sakshi Rani**  
Department of Computer Science & Engineering  
Chitkara University  

---

## ⚠️ Key Security Vulnerabilities
The following major vulnerabilities were identified:

- SQL / Command Injection  
- Cross-Site Scripting (XSS)  
- Hard-coded Secrets  
- Weak Cryptography  
- Lack of Input Validation  
- Buffer Overflow  
- Race Conditions  
- Insecure Dependencies  
- Path Traversal  
- Insecure Deserialization  
- Inadequate Access Control  

---

## 🧠 Root Causes
Why does AI generate insecure code?

- Training on **insecure or outdated datasets**
- Focus on **syntax, not security logic**
- **Automation bias** (developers trust AI blindly)
- Limited understanding of full application context
- Lack of security-focused prompting

---

## 🆚 Tool Comparison

| Feature | GitHub Copilot | ChatGPT | CodeWhisperer |
|--------|----------------|--------|---------------|
| Security Filtering | Limited | Moderate | Built-in |
| Vulnerability Rate | ~40% | ~28% (with prompts) | ~33% |
| Secret Detection | No | Partial | Yes |
| SAST Integration | External | External | Built-in |

---

## 🛠️ Mitigation Strategies

### 👨‍💻 Developer Level
- Use **security-aware prompts**
- Validate and sanitize all inputs
- Avoid hardcoding credentials

### 🏢 Organizational Level
- Mandatory **secure code reviews**
- Developer **security training**
- AI usage policies

### ⚙️ Technical Level
- Integrate **SAST tools** (SonarQube, Semgrep)
- Use **dependency scanning (SCA)**
- Enforce secure coding standards

---

## 📊 Methodology
- Reviewed **13 peer-reviewed research papers**
- Sources: IEEE, ACM, arXiv, USENIX
- Focused on vulnerability analysis, tool comparison, and security risks

---

## 📈 Key Findings
- AI tools can **replicate vulnerable code patterns**
- Security depends heavily on **prompt quality**
- AI increases risk for **inexperienced developers**
- Vulnerabilities are **systematic, not accidental**

---

## 🚀 Future Work
- Real-time AI code security analysis in IDEs  
- Standardized benchmarks for AI-generated code  
- Improved secure training datasets  
- Better human-AI collaboration models  

---

## 📚 Research Paper
The complete paper is available in this repository.

---

## 🙏 Acknowledgment
We thank the faculty of the Computer Science Department and the research community for their guidance and support.

---

## 📬 Contact
📧 Palak632.be22@chitkara.edu.in  
📧 sakshi2229.be22@chitkara.edu.in  


---

## ⭐ Support
If you found this useful, consider giving this repo a ⭐
