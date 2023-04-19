from typing import List, Optional, Any, TYPE_CHECKING

from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class DeepinProfile(XorgProfile):
	def __init__(self):
		super().__init__('Deepin', ProfileType.DesktopEnv, description='')

	@property
	def packages(self) -> List[str]:
		return [
			"deepin",
			"deepin-terminal",
			"deepin-editor"
		]

	@property
	def default_greeter_type(self) -> Optional[GreeterType]:
		return GreeterType.Lightdm

	def preview_text(self) -> Optional[str]:
		text = str(_('Environment type: {}')).format(self.profile_type.value)
		return text + '\n' + self.packages_text()