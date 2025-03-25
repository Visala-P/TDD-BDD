######################################################################
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

"""
Utility package

This package contains utility code that is not part
of any particular application
"""
from .log_handlers import init_logging

__all__ = ('init_logging',)
