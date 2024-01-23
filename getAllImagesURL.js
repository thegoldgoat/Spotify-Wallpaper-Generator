// Go to https://mytopspotify.io/ and paste this code in the console

const allImgs = document.getElementsByTagName("img");

const allURLs = [];
for (let i = 0; i < allImgs.length; i++) {
  const curImg = allImgs[i];
  // Should skip the profile picture, but I am not sure if it always has the same alt text
  if (curImg.alt === "undefined profile picture") continue;
  allURLs.push(curImg.src.toString());
}

console.log(JSON.stringify(allURLs));
