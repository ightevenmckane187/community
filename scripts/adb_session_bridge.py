import subprocess
from cipher_tube import CipherTubeApiClient  # Generated in ./sdks/python

client = CipherTubeApiClient(base_url="http://localhost:8080", token="dev-bearer-token")

def sync_adb_session():
    devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    print(f"[ADB Device List]:\n{devices.stdout}")

    # Attest device session state against the core assembly
    state = client.session_service.verify(
        token="tok_live_806_cipher",
        signature="sig_0x_ightevenmckane"
    )
    print(f"[CypherTube Attestation State]: {state}")

if __name__ == "__main__":
    sync_adb_session()
