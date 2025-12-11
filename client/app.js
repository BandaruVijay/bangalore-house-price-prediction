function getBathValue() {
  const uiBathrooms = document.getElementsByName("uiBathrooms");
  for (let i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) return i + 1;
  }
  return -1;
}

function getBHKValue() {
  const uiBHK = document.getElementsByName("uiBHK");
  for (let i = 0; i < uiBHK.length; i++) {
    if (uiBHK[i].checked) return i + 1;
  }
  return -1;
}

function onPageLoad() {
  console.log("document loaded");
  const url = "/get_location_names";
  $.get(url, function (data) {
    if (data && data.locations) {
      const uiLocations = $("#uiLocations");
      uiLocations.empty();
      uiLocations.append(new Option("Choose a Location", "", true, true));
      data.locations.forEach(loc => uiLocations.append(new Option(loc)));
    }
  }).fail(function (xhr, status, err) {
    console.error("Error fetching locations:", status, err);
  });
}

function onClickedEstimatePrice() {
  const url = "/predict_home_price";
  $.post(url, {
    total_sqft: parseFloat(document.getElementById("uiSqft").value),
    bhk: getBHKValue(),
    bath: getBathValue(),
    location: document.getElementById("uiLocations").value
  }, function (data) {
    document.getElementById("uiEstimatedPrice").innerHTML =
      "<h2>" + data.estimated_price + " Lakh</h2>";
  }).fail(function (err) {
    console.error("Price request failed:", err);
  });
}

window.onload = onPageLoad;