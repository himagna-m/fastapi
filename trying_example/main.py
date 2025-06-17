from typing import TypedDict, List, Tuple, Optional, Union, Literal, Callable, Final, cast , Any

# 1. TypedDict for structured dictionaries
class Employee(TypedDict):
    id: int
    name: str
    age: int
    department: str
    salary: float
    bonus: Optional[float]  # Optional value

# 2. Literal to restrict allowed values
Department = Literal["HR", "Engineering", "Sales", "Marketing"]

# 3. Final for constants
COMPANY_NAME: Final[str] = "Tech Solutions"

# 4. Callable type
def calculate_bonus(salary: float, bonus_rate: float) -> float:
    return salary * bonus_rate

BonusCalculator = Callable[[float, float], float]

# 5. Tuple and Union example
Record = Tuple[int, Union[str, float]]

# 6. Main function using all typing features
def process_employee(emp: Employee, bonus_fn: BonusCalculator) -> None:
    print(f"Processing Employee: {emp['name']}")
    if emp['bonus'] is None:
        emp['bonus'] = bonus_fn(emp['salary'], 0.10)
    print(f"Bonus Calculated: ₹{emp['bonus']}")
    print(f"{emp['name']} works in {emp['department']} at {COMPANY_NAME}\n")

# 7. List of employees
employees: List[Employee] = [
    {"id": 1, "name": "Alice", "age": 30, "department": "Engineering", "salary": 80000, "bonus": None},
    {"id": 2, "name": "Bob", "age": 24, "department": "Sales", "salary": 50000, "bonus": None}
]

# Run the processor
for emp in employees:
    process_employee(emp, calculate_bonus)

# 8. Example of cast
raw_value: Any = "123"
numeric_value = cast(int, int(raw_value))  # manually telling the type checker
print(f"Casted value: {numeric_value}")
