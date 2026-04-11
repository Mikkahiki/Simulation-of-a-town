async function loadGame() {

    const res = await fetch("/api/state");
    const data = await res.json();

    // ✅ GAME OVER CHECK FIRST
    if (data.game_over) {

        document.getElementById("scenario-title").innerText = "Simulation Complete";

        document.getElementById("scenario-text").innerText =
            (data.state.ending || "") + "\n\n" + (data.state.analysis || "");

        document.getElementById("choice1").style.display = "none";
        document.getElementById("choice2").style.display = "none";
        document.getElementById("choice3").style.display = "none";

        return;
    }

    // ✅ NORMAL GAME UPDATE
    document.getElementById("day").innerText = data.state.day;
    document.getElementById("temp").innerText = data.state.temperature;
    document.getElementById("co2").innerText = data.state.co2_tons;
    document.getElementById("eco").innerText = data.state.economy;
    document.getElementById("pub").innerText = data.state.public;

    document.getElementById("scenario-title").innerText = data.scenario.title;
    document.getElementById("scenario-text").innerText = data.scenario.text;

    document.getElementById("choice1").innerText = data.scenario.good.text;
    document.getElementById("choice2").innerText = data.scenario.neutral.text;
    document.getElementById("choice3").innerText = data.scenario.bad.text;
}


async function makeDecision(choice) {

    await fetch("/api/decision/" + choice);
    loadGame();

}

window.onload = loadGame;