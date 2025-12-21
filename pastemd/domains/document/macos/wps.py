"""macOS WPS document placer."""

from ..base import BaseDocumentPlacer
from ....core.types import PlacementResult
from ....utils.logging import log
from ....i18n import t


class WPSPlacer(BaseDocumentPlacer):
    """macOS WPS 内容落地器"""
    
    def place(self, docx_bytes: bytes, config: dict) -> PlacementResult:
        """macOS WPS 不支持自动插入,明确报错"""
        log("macOS WPS 不支持自动插入")
        return PlacementResult(
            success=False,
            method=None,
            error=t("placer.macos_wps.not_supported")
        )
