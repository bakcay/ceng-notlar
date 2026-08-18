# Two Port Networks

## TWO PORT NETWORKS

## and

## EQUIVALENT CIRCUIT MODELS

## 1-The equipment and components used in Lab

1.1 Oscilloscope

1.2 DVM

1.3 Variac (110V-50Hz)

1.4 Resistor (2\*10K, 3\*100 ohm)

1.5 Capacitor (100nF)

## 2-Objective

In this experiment we aimed to practice our knowledge on two port network parameters and the equivalent circuit models of such circuits as name of the experiment indicates. In addition we also increase our knowledge on some special applications of instruments specifically the phase measurement by the help of oscilloscope. In this experiment we use the given two port network and measure the z and y parameters of two port network and determine the T and Π equivalent network impedances from these parameters in order to archive our goal.

## 3-Theory and Method

A port is a terminal pair where energy can be supplied or extracted. A two-port network is a four-terminal circuit in which the terminals are paired to form an input port and an output port. Figure shows the customary way of defining the port voltages and currents.

**Figure 1******

It can be seen that the port variables comply with the passive sign convention. The linear circuit connecting the two ports is assumed to be in the zero state and there are no independent sources. In other words, there is no initial energy stored in the circuit and the box in figure contains only resistors, capacitors, inductors, mutual inductance, and dependent sources. A four-terminal network named as a two-port if the net current entering each terminal pair is zero*. *This means that the current exiting the lower port terminals in figure must be equal to the currents entering the upper terminals. We meet this condition by connecting external sources and loads between the input terminal pair or between the output terminal pair. The first issue is to identify circuit parameters that characterize a two-port. In the two port analysis the only available variables are the port voltages *V*1 and *V*2, and the port currents *I*1 and *I*2. A set of two-port parameters is defined by expressing two of these four-port variables in terms of the other two variables. The available choices can be seen in table below.

**Table 1**

It can be seen that set of parameters is defined by two equations, one for each of the two dependent port variables. Each equation involves a sum of two terms, one for each of the two independent port variables. Each term cotains proportionality because the two-port is a linear circuit and superposition can be applicable. The names given the parameters indicate their dimensions (impedance and admittance), a mixture of dimensions (hybrid), or their original application (transmission lines). There are two subscripted parameters, the first subscript indicates the port at which the dependent variable appears and the second subscript the port at which the independent variable appears. Although their dimensions are not comply with network function, all two-port parameters are network functions. In general, the parameters are functions of the complex frequency variable and *s*-domain circuit analysis applies. For sinusoidal steady-state problems, we replace *s *by *j*w and use phasor circuit analysis. For purely resistive circuits, the two-port parameters are real constants and we use resistive circuit analysis. The objectives of two-port network analysis are:

1. Determine two-port parameters of a given circuit.

2. Use two-port parameters to find port variable responses for particular input sources and output loads.

The port variable responses can be found by applying node or mesh analysis to the internal circuit connecting the input and output ports. There are several reasons why we use two port analyses instead of using the circuit analyses by using mesh current and node voltage analyses or any other. First, two-port parameters can be determined experimentally without circuit analysis. Second, there are applications in power systems and microwave circuits in which input and output ports are the only places that signals can be measure. Finally, once two-port parameters of a circuit are known, it is simple to find port variable responses for different input sources or different output loads.

## Impedance Parameters

The impedance parameters are obtained by expressing the port voltages *V*1 and *V*2 in terms of the port currents *I*1 and *I*2.

V1 = z11 I1 + z12 I2

V2 = z21 I1 + z22 I2 (eq.1)

The network functions z11, z12, z21, and z22 are called the impedance parameters

or the *z*-parameters. The matrix form of these equations are

(eq.2)

where the matrix \[z\] is called the impedance matrix of a two-port network. To measure or compute the impedance parameters, we apply current or voltage at one port and leave the other port open-circuited. When we drive port 1 with port 2 open (*I*2 = 0), the expressions in equations reduce to one term, and we can find definitions of z11 and z21.

When we drive port 2 with port 1 open (*I*1 = 0), the expressions in Eq. 1 reduce to one term that define z12 and z22 as

All of these parameters are impedances with dimensions of ohms. A two-port is said to be reciprocal when the open-circuit voltage measured at one port due to a current at the other port is unchanged when the measured and other ports are interchanged. A two-port that is not pass this test is said to be nonreciprocal. Circuits containing resistors, capacitors, and inductors are always reciprocal. However if we add dependent sources to the mix this makes the two-port nonreciprocal. If a two-port is reciprocal, then z12 = z21.

(\*)

To prove this we apply an excitation *I*1 = *I*x at the input port and observe that Eq. (1) gives the open circuit (*I*2 =0) voltage at the output port as *V*2OC = z21*I*x. Reversing the excitation and observation ports, we find that an excitation *I*2= *I*x produces an open-circuit (*I*1=0) voltage at the input port of *V*1OC=*z*12*I*x. Reciprocity requires that *V*1OC=*V*2OC, which can only happen if *z*12=*z*21.

## Admittance Parameters

The admittance parameters are obtained by expressing the port currents *I*1 and *I*2 in terms of the port voltages *V*1 and *V*2. The resulting two-port *i*–*v *relationships are

I1 = y11 V1 + y12 V2

I2 = y21 V1 + y22 V2 (eq.7)

The network functions *y*11, *y*12, *y*21, and *y*22 are called the admittance parameters or the *y*-parameters. In matrix form these equations are

where the matrix \[y \] is called the admittance matrix of a two-port network. To measure or compute the admittance parameters, we apply current or voltage at one port and short circuit the other port. When we drive at port 1 with port 2 shorted (*V*2=0), the expressions in Eq. (7) reduce to one term that define *y*11 and *y*21 as

When we drive at port 2 with port 1 shorted (*V*1=0), the expressions in Eq. (7) reduce to one term that define *y*22 and *y*12 as

All of these network functions are admittances with dimensions of siemens. If a two-port is reciprocal, then *y*12=*y*21. This can be proved using the same process applied to the *z*-parameters. The admittance parameters express port currents in terms of port voltages, whereas the impedance parameters express the port voltages in terms of the port currents. That is to say these parameters are inverses. To see this mathematically, we multiply Eq. (2) by \[z\]- 1, the inverse of the impedance matrix.

In other words;

Comparing this result with Eq. (8), we conclude that \[y\]=\[z\]-1. That is, the admittance matrix of a two port is the inverse of its impedance matrix. This means that the admittance parameters can be derived from the impedance parameters, if \[z\]-1 exists. It can be seen that admittance and impedance parameters are not independent descriptions of a two-port network.

## Hybrid Parameters

The hybrid parameters are defined in terms of a mixture of port variables. Specifically, these parameters express *V*1 and *I*2 in terms of *I*1 and *V*2. The resulting two-port *i*–*v *relationships are

V1 = h11I1 + h12V2

I2 = h21I1 + h22V2 (eq.13)

where *h*11, *h*12, *h*21, and *h*22 are called the hybrid parameters or the *h*-parameters. In matrix form these equations are

where the matrix \[h \] is called the h-matrix of a two-port network. The *h*-parameters can be measured or calculated as follows. When we drive at port 1 with port 2 shorted (*V*2= 0), the expressions in Eq. (13) reduce to one term, and we can calculate the definitions of *h*11 and *h*21.

When we drive at port 2 with port 1 open (*I*1=0), the expressions in Eq.

(13) reduce to one term, and we can calculate the definitions of *h*12 and *h*22.

These network functions have a mixture of dimensions: *h*11 is an impedance in ohms, *h*22 is an admittance in siemens, and *h*21 and *h*12 are dimensionless transfer functions. If a two-port is reciprocal, then *h*12=-*h*21. This can be proved by the same method applied to the *z*-parameters.

## Transmission Parameters

The transmission parameters express the input-port variables *V*1 and *I*1 in terms of the output-port variables *V*2 and -*I*2. The resulting two-port *i*–*v *relationships are

V1 = AV2 - B I2

I1 = C V2 - D I2 (eq.19)

where *A*, *B*, *C*, and *D *are called the transmission parameters or the t*-*parameters. In matrix form these equations are where the matrix \[t \] is called the transmission-matrix of a two-port network.

The matrix equation shows that the independent variables are *V*2 and -*I*2. In other words the minus signs in Eqs. (19) are associated with *I*2 and not with the parameters *B *and *D*. The minus sign reverses the reference direction of the output current in figure1. The t-parameters originated in the analysis of power transmission lines, where the traditional positive reference for the receiving end current is defined in the direction of the power flow. The transmission parameters are measured or calculated with a short circuit or an open circuit at the output port. Applying the conditions for a short-circuit (*V*2= 0) or open-circuit (-*I*2=0) to Eqs. (19) we obtain the following parameter identifications.

These results are expressed as reciprocals in order to comply with the transfer functions definitions we have used. If we arrange in this way, we see that the reciprocals of the transmission parameters are all forward (input-to-output) transfer functions. If a two-port is reciprocal, then *AD-BC*=1—a result that can be proved using the same method applied to *z*-parameters.

**Figure 2******

The transmission parameters are particularly useful when two-port networks are connected in cascade, as shown in figure 2. The matrix equations for two-port networks *N*a and *N*b are

We see that the output variables for *N*a are the input variables for *N*b. This happens because the two networks are connected in an output-to-input cascade, and because the minus signs in Eqs. (19) reverse the reference directions of the output currents. If we substitute the *N*b equations into the *N*a equations we find

we realize the fact that the transmission matrix of the overall network is the matrix product of the transmission matrices of the individual two-port networks in the cascade connection:

This result can be applied for any number of two ports in cascade. This method is useful since electrical power systems and communication systems consist of many two-ports connected in cascade. In these cases, the individual matrices must be placed in the matrix product in the same order the two-ports are connected in the cascade. Since the matrix multiplication may not be commutative.

**Table 2**

## Two-port connections

In some applications we can think of a circuit as an interconnection of subcircuits, and in these cases we can apply two-port analysis. Figure 3 shows four possible interconnections of two-port subcircuits *N*a and *N*b.

**Figure 3******

We can call the subcircuits as building blocks that are interconnected in order to form a higher level circuit. We can relate the two-port parameters of the interconnection to the two-port parameters of the subcircuit building blocks. If we consider the cascade connection* *in figure 3 we can think of it the transmission and the matrix of the interconnection is

\[t \] = \[ta\]\[tb\]

where \[ta\] and \[tb\] are the transmission matrices of the subcircuits *N*a and *N*b. The circuit in figure 3(b) is called a series connection* *of two ports. It is easy to show that the impedance matrix of the interconnection is

\[z \] = \[z a\] + \[z b\]

where \[za\] and \[zb\] are the impedance matrices of subcircuits *N*a and *N*b. The circuit in figure 3(c) is called a parallel connection* *of two-port. As we can expect from network duality, the admittance matrix of this interconnection is

\[y\] = \[ya\] + \[yb\]

where \[ya\] and \[yb\] are the admittance matrices of *N*a and *N*b. Finally, figure 3(d) is called a series-parallel connection* *whose hybrid matrix is

\[h\] = \[ha\] + \[hb\]

where \[ha\] and \[hb\] are the hybrid matrices of *N*a and *N*b.

Taking these into account, we can realize that there are simple relationships between the two-port parameters of an interconnection of two-ports and the subcircuits’ two-port parameters. If we assume that the interconnections do not modify the subcircuits’ two-port parameters we can derive of these relationships. But with the fundamental requirement that the net current entering each port be zero before and after the interconnections are made. We can achieve this is for subcircuits *N*a and *N*b if we connect them to a “common ground,” as indicated in figures 3. The common ground requirement means that *N*a and *N*b must be three-terminal networks and we can compare it with four-terminal networks.

## Equivalent Networks

## T-Equivalent Network

Reciprocal networks have equivalent with no independent sources the calculations as follows;

V1=z11I1+z12I2=(z11-z12)I1+z12(I1+I2)

V2=z21I1+z22I2=z21(I1+I2)+(z22-z21)I2

=z12(I1+I2)+(z22-z12)I2

**Figure 4******

## ∏-Equivalent Network

In the calculations of the п equivalent network we use admittance parameters. The calculations are as follows;

I1=y11V1+y12V2= (y11+y12) V1 -y12 (V1-V2)

I2=y21V1+y22V2= -y21 (V2-V1) + (y22+y21) V2

= -y12 (V2-V1) + (y22+y12) V2

**Figure 5******

Phase shift measurement:

We use oscilloscope for this purpose. We use the channel2 of the input of it as horizontal input and channel1 as vertical input. If we use this method the phase between the vertical and horizontal input is the ratio of (distance between intersections of the curve with vertical axis)/(vertical high-vertical low). The angle is positive if vertical high is in the first quadrant and vertical low is in third quadrant.

Sin(Ө)=a/b

This Ө is the phase component of the vertical input with respect to horizontal input.

**Figure 6******

**Figure 7******

## Calculations done before the experiment

First we assume that output port of the given circuit as an open circuit and use the formula below to calculate the z11 parameter of the two-port as follows;

z11=V1/I1=>equivalent to the Zeq of the circuit;

Zeq1=104+(107/s)=(104(s+103))/s

(1/Zeq2)=(1/Zeq1)+(1/104) Zeq2=(104(s+103))/(2s+103)

Zeq=100+Zeq2=102(102s+101.103)/(2s+103)=8972 <-13.5 ohm

Z11=8972<-13.5 ohm =z22 since the circuit is symmetric

Z21=V2/I1=>

I1.Zeq2(103/Zeq1)=V2=> V2/I1=Zeq2(103/ Zeq1)=\[104(s+103)/(2s+103)\].\[103s/104(s+103)\]=

2660<57.86 ohm

Z21=Z12=2660<57.86 ohm since the circuit is symmetric

We can find admittance parameters by use of the conversion table as;

Y11=Y22= 10-4 siemens and Y12=Y21=3.6\*10-5 siemens

## 4- Data

Calculated and measured parameters of impedance and admittance matrixes.

Z11Z12Z21Z22Y11Y12Y21Y22Calculated8972

<-13.52660

<57.862660

<57.868972

<-13.510-4

<16.33.6\*10-5

<-84.72.7\*10-5

<-84.710-4

<16.3Measured9.1k

<-152659

<56.442674

<59.68873

<-14.481.04\*10-4

<-15.53.09\*10-5

<-87.93.26\*10-5

<-85.21.06\*10-4

<-14.51

In order to calculate impedance and admittance parameters we measured the below quantities. We use digital multimeters for measuring purposes and oscilloscope for phase measurements.

| I2=0 | V2=0 | I1=0 | V1=0 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | V2 | V1 | V1 | V2 | V1 | V2 | V2 |
| 12.29 | 3.61 | 12.28 | 12.28 | 12.28 | 3.68 | 12.28 | 12.28 |
| I1 | I1 | I1 | I2 | I2 | I2 | I2 | I1 |
| 1.35m | 1.35m | 1.28m | 0.4m | 1.384m | 1.384m | 1.297m | 0.38m |
| Ө | Ө | Ө | Ө | Ө | Ө | Ө | Ө |
| -15 | 59.6 | 15.5 | 85.2 | 14.48 | 56.44 | 14.51 | 87.9 |
| Z11 | Z21 | Y11 | Y21 | Z22 | Z12 | Y22 | Y12 |
| 9.1k <-15 | 2674 <59.6 | 1.04\*10-4 <-15.5 | 3.26\*10-5 <-85.2 | 8873 <-14.48 | 2659 <56.44 | 1.06\*10-4 <-14.51 | 3.09\*10-5 <-87.9 |

We calculate the value of the equivalent network impedances by use of the formulas in theory and method section

| T-Network Impedances | Π-Network Impedance |
| --- | --- |
| Za=2659<56.44 | ZA=1.17<-30.2 |
| Zb=8629<-32 | ZB=3.09\*10-5<92.1 |
| ZC=8536<-32 | ZC=1.208.10-4<-29.25 |

## 5- Analysis and Discussion

If we compare the experimental results and the calculated ones we observe some deviations from the calculated values. But if we take the probable errors into account these deviations are acceptable ones. There have to be errors in experiment since there is no measuring instrument without errors there may be errors that can be caused by us since we measure the phase of the wave forms by the help of the oscilloscope there can be measuring errors since oscilloscope cannot give measuring values exactly as digital instrument.

In my opinion this experiment gives opportunity to us to practice our knowledge about two port networks and also we practice our use of measuring instrument. We learn how to use oscilloscope as a phase measuring instrument.

## 6- Answer to the Questions

## 1-

in other words

than from linear algebra and its applications course

where

we can use the same procedure for the y to z conversion as follows

and

2- Since the equation given can be rearranged as follows;

Z12/(1/y11)=z21/(1/y22)=>z12.y11=z21.y22

We know that for networks which have not include independent source

Y11=y22 and z12=z21

the equation is satisfied.

The proof of the equivalence of the z12=z21 is as indicated in theory and method section.

To prove this we apply an excitation *I*1 = *I*x at the input port and observe that Eq. (1) gives the open circuit (*I*2 =0) voltage at the output port as *V*2OC = z21*I*x. Reversing the excitation and observation ports, we find that an excitation *I*2= *I*x produces an open-circuit (*I*1=0) voltage at the input port of *V*1OC=*z*12*I*x. Reciprocity requires that *V*1OC=*V*2OC, which can only happen if *z*12=*z*21

## References

www3.interscience.wiley.com

---
*Kaynak: `TWO PORT NETWORKS/TWO PORT NETWORKS.doc` — elma — 2004*
