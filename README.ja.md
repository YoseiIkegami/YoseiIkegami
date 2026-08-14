# 👨‍💻 池上 耀星 (Yosei Ikegami)

[日本語](./README.ja.md) | [English](./README.en.md) | [简体中文](./README.zh-CN.md)

フロントからバックエンド・クラウドまで横断的に対応するフルスタックエンジニア。  
2026年4月よりフリーランスとして独立。大規模基幹システムの要件定義から実装・本番運用まで一貫して担当。  
Claude Code・Cursorを実務で日常的に活用したAIネイティブな開発スタイルが強みです。

---

## 📌 基本情報
- **形態**: フリーランス（IKG Systems）
- **職種**: フルスタックエンジニア / 開発リード
- **経験年数**: 4年（2022年4月〜）
- **拠点**: 東京都
- **HP**: [ikg-systems.com](https://www.ikg-systems.com/)
- **保有資格**:
  - 応用情報技術者 (2023)
  - AWS 認定クラウドプラクティショナー (2025)
  - 基本情報技術者 (2022)

---

## 🚀 個人開発

### SHIORI — 旅の写真共有サービス
[shiori.ikg-systems.com](https://shiori.ikg-systems.com) | [GitHub](https://github.com/YoseiIkegami/shiori)

「フィルムを使い切るまで写真が見られない」体験を再現した、旅行グループ向けの写真共有Webサービス。  
同級生との旅行用に自作したものを、要望を受けてサービスとして公開。

- **Stack**: Vue 3 / Vite / Vant / vue-i18n / Supabase (Postgres・RLS・Storage・Edge Functions) / Stripe / Resend / Vercel
- 解禁前は写真をクライアントから直接読ませず、Edge Function経由で署名付きURLを発行するアクセス制御を設計
- Canvasによる画像合成パイプライン（ポラロイド枠・コメント・日付を焼き込み）とトーンカーブ処理を実装
- Stripe Checkout / Resend / 保存期限の自動削除など、サービス運用に必要な周辺機能まで構築

### SplugBot — Discord経済シミュレーションBot
少人数コミュニティ向けの経済・ゲームBot。通貨、マーケット、スロット、ポーカー、強盗システム等を実装。

- **Stack**: Python (discord.py 2.x) / SQLite / Railway
- LLMを使わない決定論的ロジックで、乱数と経済バランスの設計に注力
- レイヤー間の依存方向を制約として定義し、17前後のチャンネルを自動構築する運用設計

---

## 💼 職務経歴

### 大手ゲーム会社（2026年5月〜）
**社内基幹業務システム群の開発・保守**
- **役割**: フルスタックエンジニア（業務委託）
- **技術**: PHP / Laravel, Vue.js, TypeScript, MySQL, AWS
- **実績**:
  - メディア管理・書籍/備品管理・スタッフ管理など複数の社内システムを横断的に担当。
  - 動画対応の機能拡張、外部連携APIの新規実装、DB負荷改善まで、フロントからバックエンド・DB設計まで一気通貫で対応。
  - 新機能の影響調査と工数見積もりを松竹梅の3案形式で提示し、ステークホルダーの意思決定を支援。
  - Claude Code / Codex を実務ワークフローに組み込み、開発速度と品質を両立。

### Webシステム開発会社（2024年7月〜2026年3月）
**食品流通向け基幹業務プラットフォームの開発・保守**
- **役割**: テックリード / フルスタックエンジニア
- **技術**: PHP / Laravel, React, TypeScript, AWS
- **実績**:
  - 3〜5名の開発チームを統括。タスク設計・アサイン・期日管理から、大阪／福岡への現場ヒアリング出張、要件定義、実装まで上流〜下流を主導。
  - Laravel 7 → 11 の大規模アップグレードを完遂（タスク187件・遅延0件・不具合率1.6%）。
  - CloudWatchログの解析を起点に、金額不整合など事業インパクトの大きい障害を特定・修正・再発防止まで対応。
  - OrbStack / Cursor の導入を推進し、チームの開発環境を刷新。技術記事20件以上を社内外に共有。

### ITソリューション企業（2022年4月〜2024年6月）
**大手家電メーカー向け IoTデバイス連携アプリ開発（客先常駐）**
- **役割**: フロントエンド / バックエンドエンジニア
- **技術**: Angular, TypeScript, RxJS, AWS (Lambda, API Gateway)
- **実績**:
  - RxJSによる非同期処理の最適化により、低遅延なリアルタイムUIを実現。
  - 独自バイタルセンサーからの生体データ可視化機能を実装。
  - UI/UX改善施策への貢献により、アプリ評価を ★1.7 → ★2.3 へ改善。
  - 全社デベロッパーズサミットにて最優秀賞（社長賞）を受賞。開発予算を獲得し正式プロジェクト化。

---

## 🛠 スキルセット
- **Frontend**: TypeScript, React, Angular, JavaScript
- **Backend**: PHP (Laravel), Python3
- **Cloud**: AWS (Lambda, API Gateway, CloudWatch, EC2, S3, DynamoDB)
- **Tools**: Claude Code, Cursor, Docker (OrbStack), Git/GitHub, Figma, Postman

---

## 💡 強み
- **フルスタックな課題解決能力**  
  フロントからインフラログ調査まで横断的に対応。ビジネスインパクトの大きい不具合を迅速に特定・修正。
- **デザイン思考 × エンジニアリング**  
  デザイン理論の学習経験を活かし、UXを損なわない実装と提案が得意。
- **AIネイティブな開発スタイル**  
  Claude Code・Cursorを実務に最適化させ、開発スピードと品質を両立。

---

## 🌱 趣味・ライフスタイル
- **趣味**: サウナ / ヨガ / ケーキ・コーヒー・紅茶の探究 / イラストレーション / PCゲーム
- **旅行**: マレーシア一人旅 / 沖縄でのダイビング

---

## 🔗 リンク
- **Email**: [yosei@ikg-systems.com](mailto:yosei@ikg-systems.com)
- **Qiita**: [@yosei_ikegami](https://qiita.com/yosei_ikegami)
- **Web**: [ikg-systems.com](https://www.ikg-systems.com/)
