async function loadGame() {

    const res = await fetch("/api/state");
    const data = await res.json();

    const state = data.state;

    // ✅ GAME OVER
    if (data.game_over) {

        document.getElementById("scenario-title").innerText = "Simulation Complete";

        document.getElementById("scenario-text").innerText =
            (state.ending || "No ending available") +
            "\n\n" +
            (state.analysis || "No analysis available");

        document.getElementById("choice1").style.display = "none";
        document.getElementById("choice2").style.display = "none";
        document.getElementById("choice3").style.display = "none";

        return;
    }

    // ✅ SAFE CHECK for scenario
    if (!data.scenario) {
        console.log("Scenario not ready yet...");
        setTimeout(loadGame, 300); // retry
        return;
    }

    // ✅ NORMAL GAME UPDATE
    document.getElementById("day").innerText = state.day;
    document.getElementById("temp").innerText = state.temperature;
    document.getElementById("co2").innerText = state.co2_tons;
    document.getElementById("eco")}