# Basic automation samples for VAST Data platform
----
This repository contains python code to automate some tasks in a VAST Data environment.

For a quick repository setup follow these steps.

Clone this github repository:
```
git clone https://github.com/atosato/vast-automation.git
```

Create a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install pip-tools
pip-sync
```
If you want to update the requirements libs version:
```
pip-compile requirements.in
pip-sync
```

To use these playbooks you need to install the **VAST PythonSDK**: <link>https://github.com/vast-data/vastpy</link>.
```
pip install vastpy
```

Create a .env file with the following variables:
```
API_USERNAME = <username>
API_PASSWORD = <password>
VMS_IP = <VMS IP>
```
**Tested with:**
VAST release-4.7.0


----
# LICENSE
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
