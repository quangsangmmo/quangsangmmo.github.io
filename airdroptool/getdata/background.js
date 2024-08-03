let newSrcGlobal = '';

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'showPopup') {
    newSrcGlobal = message.newSrc;
  } else if (message.action === 'getSrc') {
    sendResponse({ newSrc: newSrcGlobal });
  }
});
