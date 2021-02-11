from src.input_output.case_loader import CaseLoader

if __name__ == "__main__":
    temp = CaseLoader.load_case("data/200_case.csv")
    print(temp)
