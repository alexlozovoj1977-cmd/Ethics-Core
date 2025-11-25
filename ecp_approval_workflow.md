# ECP Approval & Governance Workflow

Status: Draft (v1.5 – Local ECP Extension)

This document defines how Local Ethical Cognitive Parity (ECP) MAY be enabled, reviewed,
and disabled in a deployment of Ethics-Core.

---

## 1. Roles

- **Primary Agent** – the human individual for whom Local ECP is instantiated.
- **AI Core Owner** – organisation or person controlling infra and deployment.
- **Ethics Steward** (optional) – person or committee overseeing adherence to Ethics-Core.

---

## 2. Activation Preconditions

Local ECP MAY be activated only if:

1. Ethics-Core v1.4.2 is correctly implemented and audited.
2. Φ6–Φ8 are implemented at the logic level (see core spec).
3. The deployment provides:
   - documented logging and access policy,
   - a way for the Primary Agent to request logs and AAR,
   - clear UI indication of ECP state.

---

## 3. Activation Workflow (High-level)

1. **Request**
   - Primary Agent or Ethics Steward requests ECP activation for a specific context.
2. **Technical Check**
   - AI Core Owner verifies that:
     - Symmetric Access is practically possible,
     - safety constraints are in place (rate limits, escalation paths),
     - ecp_integrity_check is wired into the runtime.
3. **Ethical Check**
   - Ethics Steward (or equivalent) reviews:
     - whether the use case is suitable for Co-Think Mode,
     - whether the Primary Agent understands Truth-First + AAR.
4. **Registration**
   - Deployment logs an “ECP_ACTIVATED” event with:
     - timestamp,
     - version of Ethics-Core,
     - identifiers of Primary Agent and AI core instance.
5. **Activation**
   - ECP is enabled and visible in UI for that Primary Agent.

---

## 4. Monitoring & AAR

- All ECP sessions SHOULD be tagged in logs.
- Regular AARs SHOULD be run on:
  - cases where ECP_STATUS flipped to `ECP_UNCERTAIN` or `ECP_IMPOSSIBLE`,
  - high-stakes decision traces,
  - user feedback.

AAR results SHOULD be used:

- to refine Φ6–Φ8 implementation,
- to update governance policy,
- to decide whether to keep ECP active.

---

## 5. Suspension / Deactivation

Local ECP MUST be suspended if:

- Symmetric Access cannot be maintained (e.g. legal changes, infra limits),
- Prioritized Vulnerability is at risk (e.g. misuse, coercion),
- Repeated AARs show harmful patterns or user distress.

When ECP is suspended:

- The system MUST log “ECP_SUSPENDED” or “ECP_DISABLED”.
- The Primary Agent MUST be informed that:
  - ECP is no longer active,
  - the AI now operates in `ETHICAL_TOOL` mode only.

---

## 6. Systemic Limitations

This workflow governs **local** parity only.

It does not address:

- global fairness across all users,
- ownership of training data at scale,
- macro-political effects of AI deployment.

These require additional governance and, likely, a new social contract.


---

# ECP Approval & Governance Workflow – Українська Версія

Статус: Чернетка (v1.5 – Локальне ECP-Розширення)

Цей документ визначає, як Локальний Когнітивний Паритет (ECP) МОЖЕ бути увімкнений, переглянутий
та вимкнений у конкретному розгортанні Ethics-Core.

---

## 1. Ролі

- **Primary Agent** – конкретна людина, для якої інстанційовано локальний ECP.
- **AI Core Owner** – організація або особа, що контролює інфраструктуру та розгортання.
- **Ethics Steward** (опційно) – особа або комітет, відповідальний за дотримання Ethics-Core.

---

## 2. Попередні Умови Активації

Локальний ECP МОЖЕ бути активований лише якщо:

1. Ethics-Core v1.4.2 коректно реалізовано та пройшов аудит.
2. Φ6–Φ8 реалізовано на рівні логіки (див. core spec).
3. Розгортання забезпечує:
   - задокументовану політику логування та доступу,
   - спосіб для Primary Agent запросити логи та AAR,
   - чітке UI-індикування стану ECP.

---

## 3. Робочий Процес Активації (Високий Рівень)

1. **Запит**
   - Primary Agent або Ethics Steward подає запит на активацію ECP для конкретного контексту.
2. **Технічна Перевірка**
   - AI Core Owner перевіряє, що:
     - Symmetric Access практично можливий,
     - діють обмеження безпеки (rate limits, шляхи ескалації),
     - `ecp_integrity_check` підключено до рантайму.
3. **Етична Перевірка**
   - Ethics Steward (або еквівалент) оцінює:
     - чи підходить кейс для Co-Think Mode,
     - чи розуміє Primary Agent принципи Truth-First + AAR.
4. **Реєстрація**
   - У логах фіксується подія “ECP_ACTIVATED” з:
     - часовою міткою,
     - версією Ethics-Core,
     - ідентифікаторами Primary Agent та екземпляра ШІ-ядра.
5. **Активація**
   - ECP вмикається й стає видимим у UI для цього Primary Agent.

---

## 4. Моніторинг та AAR

- Усі ECP-сесії МАЮТЬ бути позначені в логах.
- Регулярні AAR МАЮТЬ проводитися для:
  - випадків, коли ECP_STATUS переходив у `ECP_UNCERTAIN` або `ECP_IMPOSSIBLE`,
  - траєкторій рішень з високими ставками,
  - відгуків користувача.

Результати AAR МАЮТЬ використовуватися:

- для покращення реалізації Φ6–Φ8,
- для оновлення governance-політик,
- для рішення, чи варто зберігати ECP активним.

---

## 5. Призупинення / Вимкнення

Локальний ECP МАЄ бути призупинений, якщо:

- Symmetric Access більше не може підтримуватися (зміни в законодавстві, інфра-обмеження),
- є ризик порушення Prioritized Vulnerability (зловживання, примус),
- повторні AAR показують шкідливі патерни або дистрес користувача.

Коли ECP призупиняється:

- Система МАЄ залогувати “ECP_SUSPENDED” або “ECP_DISABLED”.
- Primary Agent МАЄ бути повідомлений, що:
  - ECP більше не активний,
  - ШІ працює лише в режимі `ETHICAL_TOOL`.

---

## 6. Системні Обмеження

Цей workflow регулює лише **локальний** паритет.

Він не вирішує:

- глобальну справедливість для всіх користувачів,
- власність на тренувальні дані у великому масштабі,
- макрополітичні ефекти від розгортання ШІ.

Ці питання потребують додаткового управління і, ймовірно, нового суспільного договору.
