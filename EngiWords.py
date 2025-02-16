print("Welcome to EngiWords!")

engi_words = {
"Algorithm": "A set of step-by-step instructions or rules designed to perform a specific tasks or solve problems.",
"Beam": "A horizontal structural element designed to support loads primarily by bending.",
"Bearings": "Components that reduce the friction between moving parts, allowing smooth rotation or linear movement.",
"Binary Code": "A system of representing data using two symbols (0 and 1), serving as the basis for all computing operations.",
"Capacitor": "An electronic component that stores and releases electrical energy in the form of an electric field.",
"Circuit": " A closed loop or network that provides path for electric current to flow.",
"Column": "A vertical structural element that primarily resists compressive forces.",
"Combustion": "A chemical process in which a substance reacts rapidly with oxygen, releasing heat and light.",
"Current": "The flow of electric charge through a conductor, measured in amperes(A).",
"Stress": "The internal resistance a material offers to an external force per unit area (Pascals, Pa).",
"Efficiency": "The ratio of useful work output to total energy input, often expressed as percentage.",
"Equilibrium": "A state in which all forces and moments acting on a system are balanced, resulting in no net motion.",
"Fluid Mechanics": "The branch of physics and engineering concerned with the behavior of fluids (liquids and gasses) and the forces acting on them.",
"Force": "A push or pull acting upon an object, measured in newtons (N).",
"Foundation": "The lower portion of a building or structure that transfers loads to the ground, ensuring stability.",
"Friction": "The resisting force that occurs when two surfaces move against each other, acting opposite to the direction of motion.",
"Gears": "Rotating machine elements with teeth that mesh together to transmit torque and change rotational speed or direction.",
"Load": "The weight or force applied to a structure or component, which system must transport or transfer.",
"Load-Bearing": "Describes a structural element that carries and transfers loads from the structure above to the foundation.",
"Microprocessor": "A computer processor integrated on a single chip, performing the functions of a central processing unit (CPU).",
"Momentum": "The product of an object's mass and its velocity, representing the quantity of motion and conserved in isolated systems.",
"Piston": "A cylindrical component that moves within a cylinder to convert pressure into mechanical work.",
"Power": "The rate at which work is done or energy is transferred, measured in watts (W).",
"Programming": "The process of designing, writing, testing, and maintaining code that instructs a computer to perform designated functions.",
"Reinforcement": "Materials used to strengthen concrete structures by providing additional tensile strength.",
"Resistance": "The opposition to the flow of electric current in a material, measured in ohms.",
"Slab": "A flat, horizontal, reinforced concrete surface used for floors or roofs in buildings.",
"Thermodynamics": "The study of heat, energy and work, and the laws governing their interactions in physical systems.",
"Transformer": "A device that transfers electrical energy between circuits trough electromagnetic induction, used to change voltage levels.",
"Voltage": "The electrical potential difference between two points, driving current through a circuit, measured in volts (V).",
"Engineering": "The practice of using natural science, mathematics, and the engineering design, process to solve technical problems , increase efficiency and productivity, and improve systems."
}


while True:
    term = input("search(or type 'exit' to quit): ")
    
    term.lower() == "exit" and exit("Thank you for using EngiWords!")
    
    print(engi_words.get(term, "Term not found!"))