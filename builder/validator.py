def validate_config(config):
    assert "pipeline" in config, "Config must have a 'pipeline' key"
    for step in config["pipeline"]:
        assert "type" in step, f"Step missing 'type': {step}"
        assert "name" in step, f"Step missing 'name': {step}"
