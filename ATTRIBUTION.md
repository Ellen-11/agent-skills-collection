# 出处与许可（Attribution）

本仓库中的 skill 均收集自以下开源仓库，按原样收录（仅调整了目录分组），许可文件随各 skill 文件夹一同保留。

## 来源仓库

### 1. [anthropics/skills](https://github.com/anthropics/skills)

Anthropic 官方 Agent Skills 仓库（约 186k★）。收录的 skill：

| 本仓库路径 | 原路径 | 许可 |
|---|---|---|
| `office/docx` | `skills/docx` | 见文件夹内 `LICENSE.txt` |
| `office/pptx` | `skills/pptx` | 见文件夹内 `LICENSE.txt` |
| `office/xlsx` | `skills/xlsx` | 见文件夹内 `LICENSE.txt` |
| `office/pdf` | `skills/pdf` | 见文件夹内 `LICENSE.txt` |
| `office/doc-coauthoring` | `skills/doc-coauthoring` | 见文件夹内 `LICENSE.txt` |
| `office/internal-comms` | `skills/internal-comms` | 见文件夹内 `LICENSE.txt` |
| `art/canvas-design` | `skills/canvas-design` | 见文件夹内 `LICENSE.txt` |
| `art/algorithmic-art` | `skills/algorithmic-art` | 见文件夹内 `LICENSE.txt` |
| `art/frontend-design` | `skills/frontend-design` | 见文件夹内 `LICENSE.txt` |
| `art/theme-factory` | `skills/theme-factory` | 见文件夹内 `LICENSE.txt` |

### 2. [heydamir/unslop](https://github.com/heydamir/unslop)

（约 4.6k★，CC-BY-4.0）。收录的 skill：

| 本仓库路径 | 原路径 | 许可 |
|---|---|---|
| `art/unslop` | `skills/unslop` | CC-BY-4.0（见原仓库 LICENSE） |

## 本地加固补丁（与上游的差异）

收录时对上游 pdf / pptx 的脚本做了少量本地安全加固，其余代码与上游一致：

- 新增 `scripts/pathguard.py`（pdf 与 pptx 各一份）：命令行路径参数统一校验——拒绝 NUL/换行注入、拒绝符号链接输入、输出路径的父目录必须已存在；
- `pptx/scripts/clean.py`：所有删除操作前校验目标位于解包目录内且不是符号链接，防止恶意构造的文档借清理逻辑波及目录外文件。

背景：本地安全钩子（Mimosa）将"CLI 脚本接收路径参数并写文件"一律判为路径穿越高危并拦截提交。经评估属结构性误报（这些脚本本就由 agent 在本地按需运行、路径来自使用者），经仓库所有者确认后本次提交绕过钩子；上述补丁仍保留，用于收敛真实风险面。

## 收录日期

2026-11-01，基于各仓库 main 分支当时的快照。
