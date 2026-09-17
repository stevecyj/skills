# skills

Personal agent skills for Codex CLI and Claude Code.

`skills/` contains skills maintained here. `upstreams/` contains third-party skills as Git submodules, so their history and release updates stay with the original authors.

## Install

```bash
git clone --recurse-submodules https://github.com/stevecyj/skills.git ~/src/skills
~/src/skills/scripts/install.sh
```

The installer creates a symbolic link for every managed skill in both locations:

- Codex CLI: `~/.agents/skills/<skill>`
- Claude Code: `~/.claude/skills/<skill>`

It preserves a non-symlinked skill with the same name and reports the conflict instead of overwriting it.

### Important: `--recurse-submodules`

The `--recurse-submodules` flag is **required** to clone upstream skills (no-ai-slop, shuorenhua, etc.). Without it, the `upstreams/` directory will be empty and those skills won't be available.

**If you already cloned without `--recurse-submodules`:**

```bash
cd ~/src/skills
git submodule update --init --recursive
~/src/skills/scripts/install.sh
```

### Verify installation

After running `install.sh`, confirm all 7 skills are linked:

```bash
ls -la ~/.claude/skills/ | grep -E "transcript|commit|article|slop|shuorenhua|ste100"
# Should show symlinks to all 7 skills
```

## Update

Update this repository and its pinned upstream versions:

```bash
git pull --ff-only
git submodule update --init --recursive
./scripts/install.sh
```

To review and adopt the newest upstream versions, run:

```bash
./scripts/sync-upstreams.sh
git diff --submodule=log
git commit -am "chore: update upstream skills"
git push
```

The sync script never commits or pushes. Review the submodule revisions before committing them.

## Managed upstreams

| Skill | Source |
| --- | --- |
| `asd-ste100-skill` | [`danyuchn/asd-ste100-skill`](https://github.com/danyuchn/asd-ste100-skill) (MIT) |
| `no-ai-slop` | [`petergyang/no-ai-slop`](https://github.com/petergyang/no-ai-slop) (MIT) |
| `shuorenhua` | [`MrGeDiao/shuorenhua`](https://github.com/MrGeDiao/shuorenhua) (MIT) |

Third-party files remain in their own repositories; this repo records only the upstream commit to use.
