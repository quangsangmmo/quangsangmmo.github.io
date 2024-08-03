function checkAndModifyIframes() {
  document.querySelectorAll('iframe').forEach(iframe => {
    let src = iframe.getAttribute('src');
    if (src && (src.includes('tgWebAppPlatform=web') || src.includes('tgWebAppPlatform=weba'))) {
      let newSrc = src.replace('tgWebAppPlatform=web', 'tgWebAppPlatform=android')
                      .replace('tgWebAppPlatform=weba', 'tgWebAppPlatform=android');
      iframe.setAttribute('src', newSrc);

      chrome.runtime.sendMessage({
        action: 'showPopup',
        newSrc: newSrc
      });
    }
  });
}

const observer = new MutationObserver(checkAndModifyIframes);
observer.observe(document.body, { childList: true, subtree: true });
