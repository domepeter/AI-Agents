"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-gold: #ecad0a;
  --twin-blue: #209dd7;
  --twin-purple: #753991;
  --twin-bg: #0d0d10;
  --twin-surface: #16161b;
  --twin-surface-2: #1c1c22;
  --twin-border: #2a2a32;
  --twin-border-strong: #3a3a44;
  --twin-text: #ececef;
  --twin-muted: #8c8c95;
  /* Chat panel background: a subtly blue-tinted slate, distinct from the page */
  --twin-chat-bg: #141a24;
  --twin-chat-border: #273445;

  /* Modern design tokens */
  --twin-radius: 16px;
  --twin-radius-sm: 12px;
  --twin-radius-bubble: 18px;
  --twin-shadow: 0 1px 2px rgba(0,0,0,0.3), 0 8px 24px rgba(0,0,0,0.28);
  --twin-shadow-sm: 0 1px 3px rgba(0,0,0,0.25);
  --twin-accent: linear-gradient(135deg, var(--twin-gold), #f5c542);
  --twin-glow: 0 2px 12px rgba(236,173,10,0.35);
  --twin-ease: cubic-bezier(0.22, 1, 0.36, 1);
}

/* Light mode: Gradio adds `.dark` to <body> when dark; absence = light.
   Only the neutral palette flips — gold/blue/purple accents stay identical. */
body:not(.dark) {
  --twin-bg: #f4f4f6;
  --twin-surface: #ffffff;
  --twin-surface-2: #ededf0;
  --twin-border: #dcdce2;
  --twin-border-strong: #b8b8c0;
  --twin-text: #1a1a20;
  --twin-muted: #6a6a72;
  --twin-shadow: 0 1px 2px rgba(20,20,30,0.06), 0 10px 28px rgba(20,20,30,0.08);
  --twin-shadow-sm: 0 1px 3px rgba(20,20,30,0.08);
  /* Light mode chat panel: a soft blue-grey, distinct from the white page */
  --twin-chat-bg: #eaf1f7;
  --twin-chat-border: #c3d4e2;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

/* ---------- Stable layout ---------- */
.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  border-left: 3px solid transparent !important;
  border-image: var(--twin-accent) 1 !important;
  padding-left: 14px !important;
  margin: 4px 0 10px !important;
  text-align: left !important;
}

/* ---------- Subtitle / description (the "Talk to my..." line) ----------
   Gradio renders the description as its own Markdown block (a .prose <p>),
   separate from the title. Target top-level prose paragraphs while excluding
   anything inside the chatbot / message bubbles. */
.gradio-container .prose p:not(.chatbot .prose p):not(.message p):not(.message-bubble p):not(.bubble p),
.gradio-container .md p:not(.chatbot .md p):not(.message p):not(.message-bubble p):not(.bubble p),
.gradio-container h1 + p {
  font-family: Georgia, 'Iowan Old Style', 'Noto Serif', 'Times New Roman', serif !important;
  font-style: italic !important;
  font-weight: 400 !important;
  font-size: 16px !important;
  line-height: 1.5 !important;
  color: var(--twin-muted) !important;
  letter-spacing: 0.01em !important;
  padding-left: 15px !important;
  margin: 0 0 18px !important;
  text-align: left !important;
}

/* ---------- Rounded corners on structural pieces ---------- */
.chatbot, .block, .form,
button, input, textarea {
  border-radius: var(--twin-radius) !important;
}
.examples button { border-radius: var(--twin-radius-sm) !important; }

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-chat-bg) !important;
  border: 1px solid var(--twin-chat-border) !important;
  min-height: 460px !important;
  box-shadow: var(--twin-shadow) !important;
  border-radius: var(--twin-radius) !important;
  overflow: hidden !important;
  /* Feed Gradio's own fill variables so inner panels inherit the tint */
  --block-background-fill: var(--twin-chat-bg) !important;
  --background-fill-primary: var(--twin-chat-bg) !important;
  --panel-background-fill: var(--twin-chat-bg) !important;
}
/* Inner scroll/message panels paint their own background on top of the frame,
   so recolor them too (bubbles override this with higher specificity). */
.chatbot > div,
.chatbot .wrap,
.chatbot .panel,
.chatbot .bubble-wrap,
.chatbot [class*="panel-wrap"],
.chatbot [class*="bubble-wrap"] {
  background: var(--twin-chat-bg) !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: var(--twin-shadow-sm) !important;
  padding: 10px 14px !important;
  border-radius: var(--twin-radius-bubble) !important;
  animation: twin-bubble-in 0.32s var(--twin-ease) both !important;
}

@keyframes twin-bubble-in {
  from { opacity: 0; transform: translateY(6px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* ---------- Bubble backgrounds (broad to cover Gradio variants) ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: linear-gradient(135deg, var(--twin-blue), #2cb4f0) !important;
  color: #ffffff !important;
  border-bottom-right-radius: 6px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border-bottom-left-radius: 6px !important;
}

/* ---------- Purple stripe ----------
   Apply to every common bubble class for assistant rows (we don't know which
   one the running Gradio uses), then suppress on any *nested* instance so the
   stripe lands on the outermost matching element only — exactly one stripe. */
.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 2px solid var(--twin-purple) !important;
}

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* ---------- Uniform font size in bubbles ----------
   The "first paragraph different size" was caused by a leaky `.prose p:first-of-type`
   selector. Force every paragraph in a bubble to the same size. */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.55 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
}

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 12px 16px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
  box-shadow: var(--twin-shadow-sm) !important;
  transition: border-color 0.15s var(--twin-ease), box-shadow 0.15s var(--twin-ease) !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(236,173,10,0.18) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  background: var(--twin-surface) !important;
  color: var(--twin-text) !important;
  padding: 0 18px !important;
  min-height: 48px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  box-shadow: var(--twin-shadow-sm) !important;
  transition: transform 0.14s var(--twin-ease), box-shadow 0.14s var(--twin-ease),
              background 0.14s ease, color 0.14s ease, border-color 0.14s ease;
}
button:hover {
  border-color: var(--twin-gold) !important;
  color: var(--twin-gold) !important;
  transform: translateY(-1px) !important;
}
button:active { transform: translateY(0) !important; }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-accent) !important;
  border: 1px solid transparent !important;
  color: #111111 !important;
  min-height: 48px !important;
  align-self: stretch !important;
  padding: 0 16px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: var(--twin-glow) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  filter: brightness(1.06) !important;
  color: #111111 !important;
  transform: translateY(-1px) !important;
}

/* ---------- Submit-button icon: center vertically and size correctly ---------- */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #111111 !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 24px !important;
  margin-top: 16px !important;
}
/* Flex/grid variants (newer Gradio) get breathing room via gap */
.examples > div, .examples-holder > div, [data-testid="examples"] > div {
  gap: 12px !important;
}
.examples table, .examples-table {
  background: transparent !important;
  border: 0 !important;
  border-collapse: separate !important;
  border-spacing: 10px !important;
  width: 100% !important;
}
.examples td, [data-testid="examples"] td { padding: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1.5px solid var(--twin-border-strong) !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  padding: 11px 15px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  box-shadow: var(--twin-shadow-sm) !important;
  transition: transform 0.14s var(--twin-ease), border-color 0.14s ease, color 0.14s ease !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  background: var(--twin-surface) !important;
  transform: translateY(-1px) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--twin-gold) !important; }

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); border-radius: 8px; border: 2px solid transparent; background-clip: padding-box; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); background-clip: padding-box; }

/* ---------- Selection ---------- */
::selection { background: var(--twin-gold); color: #111111; }

/* ---------- Respect reduced-motion preferences ---------- */
@media (prefers-reduced-motion: reduce) {
  *, .message-row .message, .message-row .bubble, .message-row .message-bubble {
    animation: none !important;
    transition: none !important;
  }
}

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 14px 36px !important; }
  .gradio-container h1 { font-size: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
