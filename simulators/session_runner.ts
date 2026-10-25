import { CipherTubeApiClient } from '../sdks/typescript';

const client = new CipherTubeApiClient({
  environment: 'http://localhost:8080',
  token: 'dev-bearer-token'
});

async function executeSimulation() {
  console.log('=== CypherTube Interactive Session Simulator ===');
  try {
    const sessionStatus = await client.sessionService.verify({
      token: 'tok_live_806_cipher',
      signature: 'sig_0x_ightevenmckane'
    });
    console.log(`[State Transition Confirmed]: -> ${sessionStatus}`);
  } catch (err) {
    console.error('[Simulation Integrity Error]:', err);
  }
}

executeSimulation();
