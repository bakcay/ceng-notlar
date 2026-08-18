# AC - DC Conventer

## **AC-DC CONVERTER**

## **1-CONCEPTS AND SPECIFICATIONS**

**Project Objectives**

We do this project to improve our understanding of the construction processes followed during the realization of the design and we also specifically learn AC to DC converters. In addition we also improve our preparation of project.

1.2 **Project Goals******

By doing this project we are now ready for the construction that is realization of other projects and we are now have a technical experience on the realization of the software design and also experience on the software design of the projects

**Project Responsibilities**

In this project we are responsible to give the project on time and not to cheat during the steps of the project. We are also responsible for not to waste the materials used in the labs and also protect our selves against acid,base and ultraviolet light.

1.4 **Preliminary**** Specifications******

Input voltage 220VAC ±10%

Output voltage 1,5…12 VDC continuously adjustable

Output current 1A (maximum)

Output ripple < 0.1Vpp

Load regulation better than 1%

Line regulation better than 1%

## ** **** 2-CIRCUIT DESCRIPTION**

The block diagram of the circuit:

Figure 1-Block Diagram

**DESIGN**

**Transformer**:

Transformer is used to step up or step down the voltage for our purpose. In this project we use transformer as a step down transformer since our input voltage is the mains voltage that is 220V AC and we want the output to be much smaller than this mains voltage.

*P*1 = *P*2 (Ideal Transformer)

*P*1 > *P*2 (Real Transformer)

For the ideal

V1/V2=N1/N2

I1/I2=N2/N1

R1=V1/I1=N2.V2/I2 =N2.R2

Figure 2- Transformer Circuit

**Rectifier**:

Rectifier circuit is used to convert the AC input to DC input. Although it converts AC to DC the DC output of the rectifier is not smooth as we want. There are ripples in the DC output of the rectifier circuit.

We construct a full wave rectifier for our purpose and use a capacitor to smooth the output voltage of the fullwave rectifier. We use four diodes to construct the fullwave rectifier and use capacitor additionaly for the construction of the rectifier part of our design.

Figure 3 –Rectifier Circuit

**Voltage stabilizer**:

Voltage stabilizer is used to smooth the DC output of the rectifier part of our circuit. That is to say there are ripples in our DC output of the rectifier circuit and voltage stabilizer stabilize as name implies this DC output to smooth DC output.

We construct the voltage stabilizer part by using three capacitor a LM317+two diodes+one resistors as shown in figure below.

Figure 4-Voltage Stabilizer

## **3-SIMULATION RESULTS**

Transformer:

Transformer takes the mains AC input and steps down it as shown in the graph following pages.

Rectifier:

Rectifier takes the AC output of the step down transformer and converts it to DC output with ripples as shown in the graph following** **pages.

Voltage stabilizer:

Voltage stabilizer takes the output of the rectifier’s DC output wiyh ripples and smooths the DC voltage with no ripples.

## **4-**** ****TEST & MEASUREMENT RESULTS******

**4.1 Output voltage**

Vomin =1.26V (No load)

Vomin = 0.5V for IL=1A (VRpp<0.1V)

Set to Vo=5V (No load)

Vo= 4.6V for IL=1A (VRpp<0.1V)

Set to Vo=12V (No load)

Vo= 11.4V for IL=1A (VR<0.1Vpp)

Vomax = 15.3V (No load)

Vomax =13.1V for IL=1A (VR<0.1Vpp)

Not : if ripple voltage is higher than 0.1Vpp at 1A, than use the maximum current

which gives less than 0.1Vpp ripple voltage)

**4.2 Ripple Voltage**

VR= 9mV Vpp (Vo=5V, IL=1A)

VR= 11mV Vpp (Vo=12V, IL=1A)

**4.3 Line Regulation**

Set Vo=10V for Vin=220VAC

Vo=10V for Vin=198VAC (220V-10%)

ΔV=0V

Line Regulation = (ΔV/10)/(0.10)⋅100 % = 0 %

**4.4 Load Regulation**

Set Vo=10V for IL=0A

Vo=9.86V for IL=1A

ΔV=0.14V

Load Regulation = (ΔV/10)⋅100 % = 1.4 %

*Note: If you can not get I=1A, use I**max **which you can get, instead of 1A.*

**FINAL TECHNICAL SPECIFICATIONS**

Input voltage 220VAC ±10%

Output voltage 1.26-15.3 VDC continuously adjustable

Output current ….. A (maximum)

Output ripple < 0.009Vpp

Load regulation 1.4 %

Line regulation 0%

Dimensions 186×119×80mm

Weight ≅1.5 kg

## **5-DISCUSSION**

We find the results of our test are expected compared to the simulation results. I think we practice our specific knowledge on AC to DC converters by doing this project and we also pratice our design using software programs and further our construction of the hardware by the help of the software.

## **6-**** ****Appendix A: COMPLETE SCHEMATIC DIAGRAM**

Complete circuit diagram is shown below:

Figure 5- The Schematic diagram of the circuit

Bill of materials are listed below

## **7-**** Appendix B: BILL OF MATERIALS**

Transformer 4.250.000 TL

1N4001 Diode (6) 150.000TL

Positive 20 Spray (Photosensitive) 18.500.000 TL

Electrolytic Capacitor 4700µF - 25V 600,000TL

Electrolytic Capacitor 10µF - 25V (2) 400.000TL

Capacitor 100nF 100.000TL

PCB board 500.000TL

LM317T IC 450.000TL

Resistor 470 150.000TL

Solder (1m) 350.000TL

Heat Sink 350.000TL

Connection cable soft 1m 650.000TL

Female banana plug (2) 400.000TL

ON/OFF Switch 800.000TL

Potentiometer 5k 850.000TL

Fuse 250.000TL

Fuse plug 250.000TL

Power cable with plug 220V mains 450.000TL

Box 3.500.000TL

Knob 200.000TL

## **8-Appendix C: PCB**

## Figure 6 – Bottom view of PCB

Figure 7- Component placement on PCB (Top view)

## **9-Appendix D: BOX**

Figure 8- Picture of the Power Supply

Figure 9- Mechanical drawings of the box

Figure 10- Placement of the components in the box

---
*Kaynak: `AC-DC CONVENTER/AC-DC CONVENTER.doc` — ulutasba — 2004*
