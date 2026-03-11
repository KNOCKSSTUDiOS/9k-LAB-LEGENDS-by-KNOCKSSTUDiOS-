<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>9K ULTRA TITANGINE | KNOCKSSTUDiOS</title>
    <style>
        :root {
            --sovereign-pulse: #b76e79; /* Rose Gold */
            --eye-center: #00f2ff; /* Tech Cyan */
            --engine-black: #050505;
            --9k-standard: #ffffff;
        }

        body, html {
            margin: 0; padding: 0;
            background-color: var(--engine-black);
            color: var(--9k-standard);
            font-family: 'Courier New', Courier, monospace;
            overflow-x: hidden;
            height: 100%;
        }

        /* --- THE STUDIO INTRO (30th Century Standard) --- */
        #knocks-intro {
            position: fixed; top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: black;
            display: flex; justify-content: center; align-items: center;
            z-index: 9999;
            animation: engineStartup 5s forwards;
        }

        .eye-logo {
            width: 150px; height: 150px;
            border: 2px solid var(--sovereign-pulse);
            border-radius: 50%;
            display: flex; justify-content: center; align-items: center;
            box-shadow: 0 0 50px var(--sovereign-pulse);
            animation: pulseExpand 2s cubic-bezier(0.17, 0.67, 0.83, 0.67);
        }

        .eye-inner {
            width: 40px; height: 40px;
            background: var(--eye-center);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--eye-center);
        }

        /* --- THE TITANGINE INTERFACE --- */
        #engine-ui {
            padding: 50px;
            opacity: 0;
            animation: uiFadeIn 1s forwards;
            animation-delay: 4.5s;
        }

        .stat-box {
            border: 1px solid var(--sovereign-pulse);
            padding: 20px;
            margin-bottom: 20px;
            background: rgba(183, 110, 121, 0.05);
        }

        .glitch-text {
            text-transform: uppercase;
            letter-spacing: 5px;
            color: var(--sovereign-pulse);
        }

        /* --- ANIMATIONS --- */
        @keyframes pulseExpand {
            0% { transform: scale(0); opacity: 0; filter: blur(20px); }
            50% { transform: scale(1.2); opacity: 1; filter: blur(0); }
            100% { transform: scale(1); }
        }

        @keyframes engineStartup {
            0%, 80% { opacity: 1; visibility: visible; }
            100% { opacity: 0; visibility: hidden; }
        }

        @keyframes uiFadeIn {
            to { opacity: 1; }
        }
    </style>
</head>
<body>

    <div id="knocks-intro">
        <div class="eye-logo">
            <div class="eye-inner"></div>
        </div>
        <div style="position: absolute; bottom: 20%; letter-spacing: 10px; color: var(--sovereign-pulse);">
            KNOCKSSTUDiOS
        </div>
    </div>

    <div id="engine-ui">
        <header>
            <h1 class="glitch-text">9K ULTRA TITANGINE</h1>
            <p>STATUS: SOVEREIGN PULSE ACTIVE</p>
        </header>

        <main>
            <div class="stat-box">
                <h3>MISSION: 2,000 COINS FOR THE LEGENDS</h3>
                <div id="coin-counter">PROGRESS: [0000 / 2000]</div>
            </div>

            <div class="stat-box">
                <h3>ENGINE DECODING</h3>
                <pre id="binary-pulse" style="font-size: 10px; color: #444; overflow: hidden; height: 100px;"></pre>
            </div>
        </main>

        <footer>
            <p>TRADEMARK: KNOCKSSTUDiOS (The Eye in the center)</p>
        </footer >
    </div>

    <script>
        // --- THE SOVEREIGN PULSE AUDIO ---
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        function playPulse(freq, type = 'sine', duration = 1) {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = type;
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(1, audioCtx.currentTime + duration);
            gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start();
            osc.stop(audioCtx.currentTime + duration);
        }

        // --- TITANGINE LOGIC ---
        function initiateSovereignPulse() {
            console.log("KNOCKSSTUDiOS: 9K Standard Initiated.");
            playPulse(60, 'square', 2); // Heavy startup slam
            
            // Generate visual "Engine" data
            const pulseField = document.getElementById('binary-pulse');
            setInterval(() => {
                pulseField.innerText += Math.round(Math.random());
                if (pulseField.innerText.length > 500) pulseField.innerText = "";
            }, 50);
        }

        // Trigger on click to bypass browser audio restrictions
        document.body.onclick = () => {
            if (audioCtx.state === 'suspended') audioCtx.resume();
            initiateSovereignPulse();
            document.body.onclick = null; // Only trigger once
        };

        window.onload = () => {
            console.log("9K ULTRA TITANGINE: Ready for input.");
        };
    </script>
</body>
</html>
