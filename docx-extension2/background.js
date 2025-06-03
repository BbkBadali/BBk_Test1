chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === "complete" && tab.url) {
    const match = tab.url.match(/([\w-]+\.docx)/);
    if (match) {
      const filename = match[1];
      console.log("📤 Sending filename:", filename);

      fetch("http://127.0.0.1:5000/receive_filename", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ filename })
      })
      .then(res => res.json())
      .then(data => console.log("✅ Sent to Flask", data))
      .catch(err => console.error("❌ Failed to send to Flask", err));
    }
  }
});