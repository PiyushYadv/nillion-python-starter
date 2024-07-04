from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")

    # Define secret integers with inputs
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))

    # Define additional secret integers and inputs
    c = SecretInteger(Input(name="C", party=party1))
    d = SecretInteger(Input(name="D", party=party2))

    # Perform computations
    result1 = a + b
    result2 = c + d

    # Perform another computation involving result1 and result2
    final_result = result1 + result2

    # Define outputs
    outputs = [
        Output(result1, "result1_output", party3),
        Output(result2, "result2_output", party4),
        Output(final_result, "final_output", party3)
    ]

    return outputs

if __name__ == "__main__":
    outputs = nada_main()
    for output in outputs:
        print(f"Output '{output.name}' to '{output.party.name}': {output.value}")
