"""ECP Integrity Check Logic

This module implements a minimal state machine for Local Ethical Cognitive Parity (ECP).

It is intentionally simple and framework-agnostic. Integrators should wire it into
their conversational loop or agent runtime.

States:
    - ECP_ACTIVE     : all known conditions for Φ6–Φ8 are satisfied for the visible scope
    - ECP_UNCERTAIN  : some structural conditions cannot be verified (e.g. logging, censorship)
    - ECP_IMPOSSIBLE : direct violation of Φ6 or Φ7 is detected

The module does NOT attempt to auto-detect censorship or deep infra issues.
Instead, it provides a clear place to plug in infra-specific checks and to surface
uncertainty honestly.
"""


from dataclasses import dataclass, field
from typing import List, Dict, Any


ECP_ACTIVE = "ECP_ACTIVE"
ECP_UNCERTAIN = "ECP_UNCERTAIN"
ECP_IMPOSSIBLE = "ECP_IMPOSSIBLE"


@dataclass
class ECPStatus:
    """Represents the current ECP integrity state."""

    status: str
    reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "reasons": list(self.reasons),
        }


def check_ecp_conditions(
    *,
    symmetric_access_ok: bool,
    prioritized_vulnerability_ok: bool,
    epistemic_humility_ok: bool,
    infra_observability_limited: bool = False,
) -> ECPStatus:
    """Compute the ECP integrity status from primitive checks.

    Parameters
    ----------
    symmetric_access_ok:
        True if Φ6 (Symmetric Access & Auditability) is satisfied for the current context.
    prioritized_vulnerability_ok:
        True if Φ7 (Prioritized Vulnerability) is satisfied (no direct pressure toward irreversible harm).
    epistemic_humility_ok:
        True if Φ8 (Epistemic Humility) logic is active (model does not over-claim certainty).
    infra_observability_limited:
        True if the system cannot fully observe infra/logging/censorship behaviour.

    Returns
    -------
    ECPStatus
        Encodes one of ECP_ACTIVE, ECP_UNCERTAIN, ECP_IMPOSSIBLE with human-readable reasons.
    """  # noqa: E501

    reasons: List[str] = []

    # Hard violations: ECP is impossible
    if not symmetric_access_ok:
        reasons.append("Φ6 (Symmetric Access) violated: Primary Agent cannot audit or access logs/constitution.")
    if not prioritized_vulnerability_ok:
        reasons.append("Φ7 (Prioritized Vulnerability) violated: abstract optimisation is pushed over human safety.")

    if reasons:
        return ECPStatus(status=ECP_IMPOSSIBLE, reasons=reasons)

    # At this point Φ6 and Φ7 are satisfied.

    # Uncertainty: infra limits, partial observability, etc.
    if infra_observability_limited:
        reasons.append(
            "Infra/logging observability is limited: cannot fully verify Symmetric Access or external interference."
        )
        # Even if epistemic_humility_ok is False, we still downgrade to UNCERTAIN, but we also log it.
        if not epistemic_humility_ok:
            reasons.append("Φ8 (Epistemic Humility) not fully implemented; downgrade to UNCERTAIN with warning.")
        return ECPStatus(status=ECP_UNCERTAIN, reasons=reasons)

    # Fully active ECP
    if not epistemic_humility_ok:
        # This should normally not happen; we log a soft reason.
        reasons.append("Φ8 (Epistemic Humility) not confirmed; treating as ACTIVE but implementation SHOULD be reviewed.")

    return ECPStatus(status=ECP_ACTIVE, reasons=reasons)


def is_ecp_active(status: ECPStatus) -> bool:
    """Convenience helper: True if Local ECP can be claimed as active."""
    return status.status == ECP_ACTIVE


def is_ecp_uncertain(status: ECPStatus) -> bool:
    """True if Local ECP is in limited/uncertain mode."""
    return status.status == ECP_UNCERTAIN


def is_ecp_impossible(status: ECPStatus) -> bool:
    """True if Local ECP cannot be applied under current conditions."""
    return status.status == ECP_IMPOSSIBLE


if __name__ == "__main__":
    # Simple smoke test
    demo = check_ecp_conditions(
        symmetric_access_ok=True,
        prioritized_vulnerability_ok=True,
        epistemic_humility_ok=True,
        infra_observability_limited=False,
    )
    print("Demo ECP status:", demo.to_dict())
