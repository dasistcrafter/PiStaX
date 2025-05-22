![Screenshot 2025-05-02 194327](https://github.com/user-attachments/assets/88ce0c0c-4a21-4b0f-ae87-dd90801dfca3)

# The Modular Mini Computer

This is a fully modular minicomputer based on the Raspberry Pi Zero 2W.
The example layers include a main part with the Raspberry Pi and an I/O extender.
The top layer contains a screen and a keyboard (for more info on the keyboard, see the license section).
--------------------------------------------------------------------------------------------------------

# Design Guideline

<details>
<summary>Module Connector Specs</summary>

The connector between modules is made of 4 parts (2× male / 2× female)

| Part                  | Description      | LCSC-Part-Nr |
| --------------------- | ---------------- | ------------ |
| 2×2 Connector male    | USB data/power   | C3294460     |
| 2×2 Connector female  | USB data/power   | C27983455    |
| 2×20 Connector male   | Raspberry Pi I/O | C3294478     |
| 2×20 Connector female | Raspberry Pi I/O | C3975165     |

The power is preferably transferred over the USB header and **not** over the Raspberry Pi pins directly.
If possible, use a GND and VCC layer.

</details>

<details>
<summary>Layout</summary>

The PCB should always be compliant with:
**ISO/IEC 7810 ID-1**
Size: 85.60 by 53.98 millimeters with rounded corners (radius: 2.88 mm).
The mounting holes are 2.2 mm in diameter and spaced 3 mm away from the outline.

![image](https://github.com/user-attachments/assets/9bb3eb75-5a81-4099-8094-cd261f3125ad)

**The module connectors should be placed at the following positions:**

| Part                  | X     | Y    |
| --------------------- | ----- | ---- |
| 2×2 Connector male    | 0     | 17.9 |
| 2×2 Connector female  | -29.2 | 17.9 |
| 2×20 Connector male   | 0     | 17.9 |
| 2×20 Connector female | -29.2 | 17.9 |

To connect top and bottom layers, it is best to use **vias**:

![image](https://github.com/user-attachments/assets/1473cc21-39cc-4576-abc3-eed4ca84936b)

</details>

<details>
<summary>Electrical characteristics</summary>
The bord is equipped with a 5.0V supply over the USB connector. This power supply is directly dependent on the used USB power supply and the 
Additional bords should use ths lane due to more isolated and bigger pcb track's. 
The raspberry pi is providing a 3.3V lane. The max current, while not being specified in the official documentation, is very limited. In case your need 3.3V please consider using a voltage regulator connected to the 5V lane.
</details>

<details>
<summary></summary>
</details>
