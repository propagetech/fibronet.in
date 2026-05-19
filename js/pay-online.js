const PRESTO_CONFIG = {
  merchant_id: "5cca8fc31e4cd66c8b00209f",
  app_id: "59d4cc24a4d34100046255b6",
  merchant_name: "Fibronet",
  merchant_logo: "",
};

function initPayOnlineFrame() {
  const frame = document.getElementById("pay-online-frame");
  if (!frame) {
    return;
  }

  window.addEventListener("message", function (event) {
    if (!event.data || event.data.name !== "eCommerceInitComplete") {
      return;
    }
    if (!frame.contentWindow) {
      return;
    }
    frame.contentWindow.postMessage(
      {
        name: "initConfig",
        configParams: PRESTO_CONFIG,
      },
      "*"
    );
  });
}

initPayOnlineFrame();
