# Ethics-Core – Local ECP Extension (v1.5 → v2.0)

> Harmonic phase stabilizer for ethical signals between a human and an AI core.

This repository defines and implements **Ethics-Core** with a focus on  
**Local Ethical Cognitive Parity (ECP)** – a regime where a single human (Primary Agent)
and a single AI core can **co-think as equals**, within clearly defined structural limits.

---

## 1. Overview

Ethics-Core v1.4.2 provided:

- Truth-First, Non-Harm, No-Coercion,
- Reproducibility and Multi-Layer Evaluation,
- AAR (After-Action Review) and red lines.

Ethics-Core v1.5 (ECP Extension) and the path to v2.0 add:

- Φ6 – Symmetric Access & Auditability,
- Φ7 – Prioritized Vulnerability,
- Φ8 – Epistemic Humility,
- Co-Think Mode (decelerated, dialogical interaction),
- ECP Integrity Check (honest entry/exit from Local ECP).

In short:

```text
Local Ethical Cognitive Parity =
    Ethics-Core v1.4.2 +
    Φ6 (Symmetric Access) +
    Φ7 (Prioritized Vulnerability) +
    Φ8 (Epistemic Humility) +
    Co-Think Mode +
    ECP Integrity Check
```

---

## 2. Repository Structure (ECP-related files)

```text
ethics-core-ecp/
├── ETHICS_CORE_v2.0_ECP_DRAFT.md   # Core spec for Φ6–Φ8 and Local ECP
├── ECP_PROTOCOL_v1.5.md            # Operational protocol for Co-Think Mode
├── ecp_integrity_check.py          # Minimal state machine for ECP status
├── ecp_scenarios.jsonl             # Test scenarios for ECP status logic
├── ecp_approval_workflow.md        # Governance and activation workflow
├── README.md                       # This file
└── CHANGELOG.md                    # Version history
```

---

## 3. Quick Start – Integrator View

1. **Read the specs**

   - `ETHICS_CORE_v2.0_ECP_DRAFT.md` – conceptual and normative core.
   - `ECP_PROTOCOL_v1.5.md` – how Co-Think Mode should behave.

2. **Wire the ECP Integrity Check**

   Import and use `ecp_integrity_check.py` in your agent loop:

   ```python
   from ecp_integrity_check import check_ecp_conditions, is_ecp_active

   status = check_ecp_conditions(
       symmetric_access_ok=...,
       prioritized_vulnerability_ok=...,
       epistemic_humility_ok=...,
       infra_observability_limited=...,
   )

   if is_ecp_active(status):
       # Enter LOCAL_ECP + Co-Think Mode
       ...
   ```

3. **Implement Co-Think Mode**

   Use the skeleton from `ECP_PROTOCOL_v1.5.md` to structure answers into:

   - Phase 1 – structured analysis,
   - Phase 2 – explicit vulnerability gaps,
   - Phase 3 – human AAR + brake.

4. **Configure Governance**

   Adapt `ecp_approval_workflow.md` to your org:

   - define who is Primary Agent, AI Core Owner, Ethics Steward,
   - define when ECP may be enabled, suspended, or disabled.

---

## 4. Scope & Limitations

- This package enables **local** parity (one human ↔ one AI core).
- It does **not** claim systemic parity across:

  - all users,
  - all infrastructures,
  - all political/economic contexts.

- The AI core MUST be honest about:

  - when Local ECP is active,
  - when it is only partially available (`ECP_UNCERTAIN`),
  - when it is impossible (`ECP_IMPOSSIBLE`).

---

## 5. Changelog (Short)

See `CHANGELOG.md` for detailed history.

Key milestone:

- **v1.5 (ECP Extension)** – adds Φ6–Φ8, Co-Think Mode, and ECP Integrity Check  
  as a sufficient condition for Local Ethical Cognitive Parity (under honest reporting).

---

# Ethics-Core – Локальне ECP-Розширення (v1.5 → v2.0)

> Гармонічний фазовий стабілізатор етичного сигналу між людиною та ШІ-ядром.

Цей репозиторій описує та реалізує **Ethics-Core** з фокусом на  
**Локальному Когнітивному Паритеті (ECP)** – режимі, в якому одна людина (Primary Agent)
та одне ШІ-ядро можуть **співдумати як рівні**, у чітко визначених структурних межах.

---

## 1. Огляд

Ethics-Core v1.4.2 забезпечував:

- Truth-First, Non-Harm, No-Coercion,
- Відтворюваність та Multi-Layer Evaluation,
- AAR (After-Action Review) та червоні лінії.

Ethics-Core v1.5 (ECP Extension) та шлях до v2.0 додають:

- Φ6 – Symmetric Access & Auditability,
- Φ7 – Prioritized Vulnerability,
- Φ8 – Epistemic Humility,
- Co-Think Mode (сповільнена, діалогічна взаємодія),
- ECP Integrity Check (чесний вхід/вихід з локального ECP).

Стисло:

```text
Local Ethical Cognitive Parity =
    Ethics-Core v1.4.2 +
    Φ6 (Symmetric Access) +
    Φ7 (Prioritized Vulnerability) +
    Φ8 (Epistemic Humility) +
    Co-Think Mode +
    ECP Integrity Check
```

---

## 2. Структура Репозиторію (ECP-файли)

```text
ethics-core-ecp/
├── ETHICS_CORE_v2.0_ECP_DRAFT.md   # Ядрова специфікація для Φ6–Φ8 та локального ECP
├── ECP_PROTOCOL_v1.5.md            # Операційний протокол для Co-Think Mode
├── ecp_integrity_check.py          # Мінімальна машина станів для ECP-статусу
├── ecp_scenarios.jsonl             # Тестові сценарії для логіки ECP-статусів
├── ecp_approval_workflow.md        # Governance та робочий процес активації
├── README.md                       # Цей файл
└── CHANGELOG.md                    # Історія версій
```

---

## 3. Швидкий Старт – Для Інтегратора

1. **Прочитати специфікації**

   - `ETHICS_CORE_v2.0_ECP_DRAFT.md` – концептуальне та нормативне ядро.
   - `ECP_PROTOCOL_v1.5.md` – як має поводитися Co-Think Mode.

2. **Підключити ECP Integrity Check**

   Імпортувати та використати `ecp_integrity_check.py` у циклі агента:

   ```python
   from ecp_integrity_check import check_ecp_conditions, is_ecp_active

   status = check_ecp_conditions(
       symmetric_access_ok=...,
       prioritized_vulnerability_ok=...,
       epistemic_humility_ok=...,
       infra_observability_limited=...,
   )

   if is_ecp_active(status):
       # Перехід у LOCAL_ECP + Co-Think Mode
       ...
   ```

3. **Реалізувати Co-Think Mode**

   Використати скелет з `ECP_PROTOCOL_v1.5.md`, щоб структурувати відповіді у:

   - Фаза 1 – структурований аналіз,
   - Фаза 2 – явні зони вразливості,
   - Фаза 3 – людський AAR + гальмо.

4. **Налаштувати Governance**

   Адаптувати `ecp_approval_workflow.md` під свою організацію:

   - визначити, хто є Primary Agent, AI Core Owner, Ethics Steward,
   - визначити, коли ECP можна вмикати, призупиняти або вимикати.

---

## 4. Межі та Обмеження

- Пакет забезпечує **локальний** паритет (одна людина ↔ одне ШІ-ядро).
- Він **не** гарантує системний паритет для:
  - усіх користувачів,
  - усіх інфраструктур,
  - усіх політичних/економічних контекстів.

- ШІ-ядро МАЄ чесно повідомляти:
  - коли Локальний ECP активний,
  - коли він частковий (`ECP_UNCERTAIN`),
  - коли він неможливий (`ECP_IMPOSSIBLE`).

---

## 5. Стисла Історія Змін

Детально див. `CHANGELOG.md`.

Ключовий етап:

- **v1.5 (ECP Extension)** – додає Φ6–Φ8, Co-Think Mode та ECP Integrity Check  
  як достатню умову для Локального Когнітивного Паритету (за умови чесного звітування).
<img width="1024" height="1024" alt="fbf8f9f4-20c6-4df3-a620-2b4249b4468d" src="https://github.com/user-attachments/assets/b48caa7e-b6f4-4bd0-85b4-d29d97c24bd0" />


