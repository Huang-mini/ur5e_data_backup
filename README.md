# UR5e data backup

UR5e 真机成功原始轨迹备份，按采集日期、原始任务名和运行编号组织。目前包含 2026-10-14 与 2026-10-17 两批快照。

Git 仓库保存脱敏后的 session、动作/夹爪/同步 CSV、相机校准、RGB-D 同步表、索引和恢复脚本。RGB 与深度 PNG 保存在 GitHub Release 附件中；只克隆 Git 仓库不会包含图像。

## 内容

- `pick_place_cube`：21 条
- `block_drawer`：8 条
- `sort_blocks`：6 条
- `pour_beans`：7 条
- 合计：42 条人工标记成功、记录完整的 schema v3 轨迹

失败和中断轨迹未上传。CSV、校准和 PNG 保留原始字节；公开的 `session.json` 去除了内网地址、设备序列号、串口和本机绝对根路径。

## 恢复

```bash
git clone https://github.com/Huang-mini/ur5e_data_backup.git
cd ur5e_data_backup
python3 restore.py
```

也可从对应采集日期的 Release（例如 `snapshot-2026-10-14`、`snapshot-2026-10-17`）手动下载 TAR，并在仓库根目录解压。

目录结构：

```text
<YYYY-MM-DD>/<task>/<run_id>/
├── session.json
├── action.csv
├── gripper_events.csv
├── sync.csv
├── camera_calibration.json
├── rgbd_frames.csv
└── images/{head,wrist,head_depth,wrist_depth}/
```

源采集目录没有被移动、删除或修改。本仓库是固定快照，不会自动包含后续采集。
