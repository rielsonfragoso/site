#!/bin/bash
cd /home/claude/site-repo && cp /home/claude/site/v2/livros_dados.py _fonte/site/ && mkdir -p _fonte/tools && cp /home/claude/site/tools/* _fonte/tools/ && git add -A && git -c user.name="Rielson Fragoso" -c user.email="rielsonfragoso@users.noreply.github.com" commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_012HgkBVM2VXHLysW3H26MLv" && git -c push.negotiate=true push -q origin main && git log --oneline -1
