# Finite Probability Demonstrations  
**Marginal, Conditional, Bayes & More**

A simple yet educational Python script that visualizes core probability concepts using finite sets and matplotlib bar charts.

<p align="center">
  <img src="https://github.com/user-attachments/assets/55d78294-0095-434f-8547-737413ad7abf" alt="Probability bar charts visualization" width="90%">
  <br><em>7 side-by-side bar plots showing marginal, joint, conditional, union, complement, total probability, and Bayes results</em>
</p>

## Concepts Visualized

This project clearly demonstrates the following probability rules:

- **Marginal probability**  
  P(A), P(B), P(Art)

- **Joint probability**  
  P(A ∩ Art), P(B ∩ Art)

- **Conditional probability**  
  P(A|Art), P(B|Art)

- **Union probability** (inclusion-exclusion)  
  P(A ∪ Art), P(B ∪ Art)

- **Complement**  
  P(¬A), P(¬B)

- **Law of total probability**  
  P(Art) = P(Art|A)·P(A) + P(Art|B)·P(B)

- **Bayes' theorem**  
  P(A|Art) and the reverse conditional P(Art|A)

All calculations are performed using basic set operations — **no probability libraries** are used.

## Example Scenario

- **Universe (sample space S)**: 9 students numbered 1 to 9  
- **Group A**: students {1,2,3,4,5} (5 members)  
- **Group B**: students {6,7,8,9} (4 members, disjoint from A)  
- **Art club**: students {4,5,6,8,9} (5 members, overlaps with both groups)

The script produces **seven aligned bar charts** that show how these probabilities behave in this concrete finite example.

## Features

- Clean, readable function names  
  (`intersection_size`, `joint_probability`, `conditional_probability`, `bayes_theorem`, …)
- Consistent use of set operations (`set(A) & set(B)`) for intersections
- Both directions of conditional probability shown in the Bayes panel
- Educational color coding (blue & orange) for P(A|Art) vs P(Art|A)
- Minimal dependencies — only `matplotlib` required
- Self-contained single-file script

## Requirements

```bash
pip install matplotlib
```
# Clone the repository
```
git clone https://github.com/Hitesh-Ojha/Finite-Probability-Demonstrations.git
```
# Enter the directory
```
cd Finite-Probability-Demonstrations
```
# Run the script
```
python Finite-Probability-Demonstrations.py
```
