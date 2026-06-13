from pydantic import BaseModel, ValidationError


class TaskModel(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False


# Valid data
task = TaskModel(
    title="Finish report",
    priority="high",
    completed=True
)

print("Valid task:")
print(task)
print()
try:
    bad_task = TaskModel(
        title=123,          
        priority=5,         
        completed="maybe"  
    )
except ValidationError as e:
    print("Validation errors:")
    for error in e.errors():
        field = ".".join(str(x) for x in error["loc"])
        print(f"- {field}: {error['msg']}")