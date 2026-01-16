# agent.vcl (VCL Agent - Real Alive with Voice/Persist)
def fill_form_agent ~hint:smart:
    ~persist:"responses.json" { data = load_if_exists() }
    vibe no_data data is None:
        ~voice:recognize { name = get_input("Name?") }
        ~voice:recognize { age = get_input("Age?") }
        save_data({'name': name, 'age': age})
    else loaded:
        print("Loaded alive: " + data['name'] + ", " + data['age'])

main:
    fill_form_agent ?? @grok{"Heal input errors"}
