import { ThirdwebStorage } from "@thirdweb-dev/storage";

// First, instantiate the thirdweb IPFS storage
const storage = new ThirdwebStorage({
  secretKey: "JuM8zX_qjaHtEB_rJ2wUv1KQCdTZJeDhwaQXIO-eXVLYqF7Ijj_DXHsAmDgTGm2IfA81_YYuB0MQ4t-sa21vZg", // You can get one from dashboard settings
});

// Here we get the IPFS URI of where our metadata has been uploaded
const uri = await storage.upload('/Users/sayandeepsharma/Downloads/Untitled.png');
// This will log a URL like ipfs://QmWgbcjKWCXhaLzMz4gNBxQpAHktQK6MkLvBkKXbsoWEEy/0
console.info(uri);

// Here we a URL with a gateway that we can look at in the browser
const url = await storage.resolveScheme(uri);
// This will log a URL like https://ipfs.thirdwebstorage.com/ipfs/QmWgbcjKWCXhaLzMz4gNBxQpAHktQK6MkLvBkKXbsoWEEy/0
console.info(url);

// You can also download the data from the uri
const data = await storage.downloadJSON(uri);