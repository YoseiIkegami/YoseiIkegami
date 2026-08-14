# 👨‍💻 池上耀星 (Yosei Ikegami)

[日本語](./README.ja.md) | [English](./README.en.md) | [简体中文](./README.zh-CN.md)

从前端到后端、云基础设施均可对应的全栈工程师。
2026年4月起以自由职业者身份独立。负责大型基干系统从需求定义到实施、生产运维的全流程。
擅长将 Claude Code 与 Cursor 融入日常实务的 AI 原生开发方式。

---

## 📌 基本信息
- **形态**: 自由职业（IKG Systems）
- **职位**: 全栈工程师 / 开发负责人
- **经验年限**: 4年（2022年4月〜）
- **所在地**: 东京
- **网站**: [ikg-systems.com](https://www.ikg-systems.com/)
- **持有资格**:
  - 应用信息处理技术者 (2023)
  - AWS 认证云从业者 (2025)
  - 基本情报技术者 (2022)

---

## 🚀 个人开发

### SHIORI — 旅行照片分享服务
[shiori.ikg-systems.com](https://shiori.ikg-systems.com) | [GitHub](https://github.com/YoseiIkegami/shiori)

面向旅行团体、再现「胶卷用完前无法查看照片」体验的照片分享 Web 服务。
最初为与同学旅行而自建，应需求公开为服务。

- **Stack**: Vue 3 / Vite / Vant / vue-i18n / Supabase (Postgres・RLS・Storage・Edge Functions) / Stripe / Resend / Vercel
- 解禁前不让客户端直接读取照片，通过 Edge Function 签发签名 URL 的访问控制设计
- 实现 Canvas 图像合成流水线（拍立得边框・评论・日期烧录）与色调曲线处理
- 构建 Stripe Checkout / Resend / 保存期限自动删除等服务运营所需周边功能

### SplugBot — Discord 经济模拟 Bot
面向小规模社区的经济与游戏 Bot。实现货币、市场、老虎机、扑克、抢劫系统等。

- **Stack**: Python (discord.py 2.x) / SQLite / Railway
- 不使用 LLM 的确定性逻辑，注重随机数与经济平衡设计
- 将层间依赖方向定义为约束，设计自动构建约 17 个频道的运营架构

---

## 💼 工作经历

### 大型游戏公司（2026年5月〜）
**社内基干业务系统群的开发与维护**
- **角色**: 全栈工程师（业务委托）
- **技术**: PHP / Laravel, Vue.js, TypeScript, MySQL, AWS
- **成果**:
  - 横跨媒体管理、书籍/备品管理、员工管理等多个社内系统。
  - 从视频功能扩展、外部联动 API 新规实现到 DB 负载改善，前端到后端・DB 设计一气呵成。
  - 以松竹梅三档方案形式提出新功能影响调查与工时估算，支持利益相关方决策。
  - 将 Claude Code / Codex 融入实务工作流，兼顾开发速度与质量。

### Web 系统开发公司（2024年7月〜2026年3月）
**食品流通基干业务平台的开发与维护**
- **角色**: 技术负责人 / 全栈工程师
- **技术**: PHP / Laravel, React, TypeScript, AWS
- **成果**:
  - 统括 3〜5 人开发团队。从任务设计・分配・期限管理到大阪/福冈现场调研出差、需求定义、实现，主导上游到下游。
  - 完成 Laravel 7 → 11 大规模升级（任务 187 件・延迟 0 件・缺陷率 1.6%）。
  - 以 CloudWatch 日志解析为起点，定位・修复・防止金额不一致等高业务影响故障的复发。
  - 推进 OrbStack / Cursor 导入，刷新团队开发环境。社内外共享技术文章 20 篇以上。

### IT 解决方案企业（2022年4月〜2024年6月）
**面向大型家电制造商的 IoT 设备联动应用开发（驻场）**
- **角色**: 前端 / 后端工程师
- **技术**: Angular, TypeScript, RxJS, AWS (Lambda, API Gateway)
- **成果**:
  - 通过 RxJS 异步处理优化，实现低延迟实时 UI。
  - 实现自有生命体征传感器生物数据可视化功能。
  - 通过 UI/UX 改善贡献，将应用评分从 ★1.7 提升至 ★2.3。
  - 在全社开发者峰会获最优秀奖（社长奖），获得开发预算并正式项目化。

---

## 🛠 技能
- **Frontend**: TypeScript, React, Angular, JavaScript
- **Backend**: PHP (Laravel), Python3
- **Cloud**: AWS (Lambda, API Gateway, CloudWatch, EC2, S3, DynamoDB)
- **Tools**: Claude Code, Cursor, Docker (OrbStack), Git/GitHub, Figma, Postman

---

## 💡 优势
- **全栈问题解决能力**  
  从前端到基础设施日志调查横跨对应。迅速定位并修复业务影响大的缺陷。
- **设计思维 × 工程**  
  活用设计理论学习经验，擅长不损害 UX 的实现与提案。
- **AI 原生开发方式**  
  将 Claude Code 与 Cursor 优化用于实务，兼顾开发速度与质量。

---

## 🌱 爱好・生活方式
- **爱好**: 桑拿 / 瑜伽 / 探索蛋糕・咖啡・红茶 / 插画 / PC 游戏
- **旅行**: 马来西亚一人旅 / 冲绳潜水

---

## 🔗 链接
- **Email**: [yosei@ikg-systems.com](mailto:yosei@ikg-systems.com)
- **Qiita**: [@yosei_ikegami](https://qiita.com/yosei_ikegami)
- **Web**: [ikg-systems.com](https://www.ikg-systems.com/)
