function extractFilenameFromURL(url) {
  const match = url.match(/\/([^\/?]+\.docx)(\?|$)/i);
  if (match && match[1]) {
    return match[1];
  }
  return null;
}

const url = window.location.href;
const filename = extractFilenameFromURL(url);

if (filename) {
  // فرستادن به Flask
  fetch('http://localhost:5000/receive_filename', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ filename })
  })
    .then(res => res.text())
    .then(data => console.log("Server responded:", data))
    .catch(err => console.error("Error sending filename to server:", err));
}