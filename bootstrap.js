// when the extension is first installed
// chrome.runtime.onInstalled.addListener(function(details) {
//     chrome.storage.sync.set({clean_news_feed: true});
// });

// listen for any changes to the URL of any tab.
// chrome.tabs.onUpdated.addListener(function(id, info, tab){
//     if (tab.url.toLowerCase().indexOf("facebook.com") > -1){
//         chrome.pageAction.show(tab.id);
//     }
// });

chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
      console.log('The color is green.');
    });
});