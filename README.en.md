# 👨‍💻 Yosei Ikegami

[日本語](./README.ja.md) | [English](./README.en.md) | [简体中文](./README.zh-CN.md)

A full-stack engineer who works across frontend, backend, and cloud.
Independent as a freelancer since April 2026. Handles large-scale core systems end to end, from requirements definition through implementation and production operations.
Strengths include an AI-native development style, using Claude Code and Cursor in daily professional workflows.

---

## 📌 Basic Information
- **Type**: Freelance (IKG Systems)
- **Role**: Full-Stack Engineer / Development Lead
- **Experience**: 4 years (since April 2022)
- **Location**: Tokyo, Japan
- **Website**: [ikg-systems.com](https://www.ikg-systems.com/)
- **Certifications**:
  - Applied Information Technology Engineer (2023)
  - AWS Certified Cloud Practitioner (2025)
  - Fundamental Information Technology Engineer (2022)

---

## 🚀 Personal Projects

### SHIORI — Travel Photo Sharing Service
[shiori.ikg-systems.com](https://shiori.ikg-systems.com) | [GitHub](https://github.com/YoseiIkegami/shiori)

A photo-sharing web service for travel groups that recreates the experience of not being able to view photos until the film is used up.
Originally built for a trip with classmates, then released as a service based on user requests.

- **Stack**: Vue 3 / Vite / Vant / vue-i18n / Supabase (Postgres, RLS, Storage, Edge Functions) / Stripe / Resend / Vercel
- Designed access control so photos are not read directly from the client before release; signed URLs are issued via Edge Functions
- Implemented a Canvas-based image compositing pipeline (Polaroid frame, comments, date burn-in) and tone curve processing
- Built operational features including Stripe Checkout, Resend, and automatic deletion by retention period

### SplugBot — Discord Economy Simulation Bot
An economy and game bot for small communities. Implements currency, markets, slots, poker, robbery systems, and more.

- **Stack**: Python (discord.py 2.x) / SQLite / Railway
- Focused on deterministic logic without LLMs, emphasizing randomness and economic balance design
- Defined dependency direction between layers as constraints and designed operations to auto-provision around 17 channels

---

## 💼 Work History

### Major Game Company (May 2026–Present)
**Development and maintenance of internal core business systems**
- **Role**: Full-Stack Engineer (Contract)
- **Tech**: PHP / Laravel, Vue.js, TypeScript, MySQL, AWS
- **Achievements**:
  - Cross-functionally handled multiple internal systems including media management, book/supplies management, and staff management.
  - End-to-end work from frontend through backend and DB design, including video feature expansion, new external integration APIs, and DB load improvements.
  - Supported stakeholder decision-making by presenting impact analysis and effort estimates in three-tier (good/better/best) options.
  - Integrated Claude Code / Codex into daily workflows to balance development speed and quality.

### Web System Development Company (July 2024–March 2026)
**Development and maintenance of a core business platform for food distribution**
- **Role**: Tech Lead / Full-Stack Engineer
- **Tech**: PHP / Laravel, React, TypeScript, AWS
- **Achievements**:
  - Led a development team of 3–5 people, from task design, assignment, and deadline management through on-site hearings in Osaka/Fukuoka, requirements definition, and implementation.
  - Completed a large-scale Laravel 7 → 11 upgrade (187 tasks, 0 delays, 1.6% defect rate).
  - Identified, fixed, and prevented recurrence of high business-impact incidents such as monetary inconsistencies, starting from CloudWatch log analysis.
  - Promoted adoption of OrbStack / Cursor to refresh the team's development environment. Published 20+ technical articles internally and externally.

### IT Solutions Company (April 2022–June 2024)
**IoT device integration app development for a major home appliance manufacturer (on-site)**
- **Role**: Frontend / Backend Engineer
- **Tech**: Angular, TypeScript, RxJS, AWS (Lambda, API Gateway)
- **Achievements**:
  - Achieved low-latency real-time UI through RxJS-based async processing optimization.
  - Implemented biological data visualization from a proprietary vital sensor.
  - Improved app rating from ★1.7 to ★2.3 through UI/UX improvement initiatives.
  - Won the Grand Prize (President's Award) at the company-wide Developers Summit and secured development budget for formal project launch.

---

## 🛠 Skillset
- **Frontend**: TypeScript, React, Angular, JavaScript
- **Backend**: PHP (Laravel), Python3
- **Cloud**: AWS (Lambda, API Gateway, CloudWatch, EC2, S3, DynamoDB)
- **Tools**: Claude Code, Cursor, Docker (OrbStack), Git/GitHub, Figma, Postman

---

## 💡 Strengths
- **Full-stack problem solving**  
  Handles issues cross-functionally from frontend through infrastructure log investigation. Quickly identifies and fixes defects with large business impact.
- **Design thinking × engineering**  
  Applies design theory learning to deliver implementations and proposals that preserve UX.
- **AI-native development style**  
  Optimizes Claude Code and Cursor for professional use to balance development speed and quality.

---

## 🌱 Hobbies & Lifestyle
- **Hobbies**: Sauna / Yoga / Exploring cakes, coffee, and tea / Illustration / PC games
- **Travel**: Solo trip to Malaysia / Diving in Okinawa

---

## 🔗 Links
- **Email**: [yosei@ikg-systems.com](mailto:yosei@ikg-systems.com)
- **Qiita**: [@yosei_ikegami](https://qiita.com/yosei_ikegami)
- **Web**: [ikg-systems.com](https://www.ikg-systems.com/)
