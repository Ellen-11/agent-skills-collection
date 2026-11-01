# Agent Skills 精选集（办公 × 美术）

从 GitHub 高星仓库中精选的 **11 个** Agent Skill（SKILL.md 格式），聚焦两类场景：

- **办公**：文档处理、数据分析、写作与沟通
- **美术**：平面/品牌设计、生成艺术、前端 UI 美术

每个 skill 均来自口碑最好的开源仓库，完整保留原目录与许可文件，出处见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 目录

### 📁 office/ —— 办公类（6 个）

| Skill | 用途 | 来源 |
|---|---|---|
| `docx` | Word 文档的创建、编辑、格式转换、修订与批注 | [anthropics/skills](https://github.com/anthropics/skills) |
| `pptx` | PPT 演示文稿从零创建、大纲转幻灯片、编辑排版 | [anthropics/skills](https://github.com/anthropics/skills) |
| `xlsx` | Excel 工作簿读写、公式、透视表、数据分析与图表 | [anthropics/skills](https://github.com/anthropics/skills) |
| `pdf` | PDF 生成、拆分合并、表单填写、转图片/文档 | [anthropics/skills](https://github.com/anthropics/skills) |
| `doc-coauthoring` | 结构化文档共创流程：提案、技术规格、决策文档 | [anthropics/skills](https://github.com/anthropics/skills) |
| `internal-comms` | 内部沟通写作：状态报告、领导层简报、FAQ、事故报告 | [anthropics/skills](https://github.com/anthropics/skills) |

### 🎨 art/ —— 美术类（5 个）

| Skill | 用途 | 来源 |
|---|---|---|
| `canvas-design` | 海报、视觉艺术等静态设计（输出 png/pdf），自带设计哲学与字体库 | [anthropics/skills](https://github.com/anthropics/skills) |
| `algorithmic-art` | p5.js 生成艺术：流场、粒子系统、种子随机与交互参数 | [anthropics/skills](https://github.com/anthropics/skills) |
| `frontend-design` | 有设计感的前端界面，避免千篇一律的 AI 味布局 | [anthropics/skills](https://github.com/anthropics/skills) |
| `theme-factory` | 10 套预设主题（配色+字体），一键应用到幻灯片/文档/落地页 | [anthropics/skills](https://github.com/anthropics/skills) |
| `unslop` | 把"一眼 AI 生成"的 UI 改造为真正有设计感的界面 | [heydamir/unslop](https://github.com/heydamir/unslop) |

## 安装使用

### 方式一：Claude Code / ZCode 等 CLI 代理

把想要的 skill 文件夹整个复制到代理的 skills 目录即可：

```bash
# Claude Code（用户级，全局可用）
cp -r office/docx ~/.claude/skills/docx

# ZCode：放到对应 workspace 或用户的 skills 目录后重启会话即可被发现
```

也可以全部安装：

```bash
cp -r office/* ~/.claude/skills/
cp -r art/* ~/.claude/skills/
```

### 方式二：claude.ai 网页版

1. 把单个 skill 文件夹压缩成 zip（例如 `canvas-design/` → `canvas-design.zip`）；
2. 打开 claude.ai → **Settings → Capabilities → Skills** → 上传 zip；
3. 对话中提到相关任务（如"帮我做一张海报"）时 skill 会自动触发。

> 注意：含 `scripts/` 的 skill（docx/pptx/xlsx/pdf/algorithmic-art 等）在网页版的代码执行环境中运行，如遇环境缺依赖，优先在 CLI 场景使用。

## 后续更新

想补充新的 skill 时，直接从以下来源挑选后复制进 `office/` 或 `art/`：

- [anthropics/skills](https://github.com/anthropics/skills)（官方，186k★）
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)（78k★ 精选清单）
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)（15k★ 精选清单）
- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)（29k★，380+ 技能大合集）
