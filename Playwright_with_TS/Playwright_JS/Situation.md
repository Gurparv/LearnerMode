how can i simulate different location in chrome.. be concise

You have a few options:

1. **Chrome DevTools (best for testing websites)**

   * Press `F12` → `Ctrl + Shift + P`
   * Type **Show Sensors** → Enter
   * In **Location**, choose a preset or **Custom location**
   * Enter **Latitude** and **Longitude**

2. **Override geolocation permission**

   * Make sure the site has **Location** permission enabled.
   * The DevTools location override only works if the site uses the browser's Geolocation API.

3. **For IP-based location (different country/city)**

   * Use a **VPN** or **proxy**. DevTools does **not** change your IP address.

**Summary:**

* **GPS/location API testing:** DevTools → Sensors → Custom Location.
* **IP/geographic region testing:** VPN or proxy.