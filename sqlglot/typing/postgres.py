from __future__ import annotations

from sqlglot import exp
from sqlglot.typing import EXPRESSION_METADATA

EXPRESSION_METADATA = {
    **EXPRESSION_METADATA,
    exp.Sign: {"annotator": lambda self, e: self._annotate_by_args(e, "this")},
}
