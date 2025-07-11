# Very simple rule without input
rule save_image:
    output:
        report("../results/astronaut.png", category="Input image"),
    log:
        "../logs/save_image/astronaut.log",
    conda:
        "../envs/environment.yaml"
    shell:
        "python scripts/create-data.py --image-name astronaut --output {output}"


# Simple rule definition
rule transform_image:
    input:
        "../results/astronaut.png",
    output:
        report(
            "../results/transformed-images/{transformation}.png",
            category="Transformed image",
        ),
    log:
        "../logs/transform_image/{transformation}.log",
    conda:
        "../envs/environment.yaml"
    shell:
        "python scripts/transform.py --image {input} --transformation {wildcards.transformation} --output {output}"


# More complex rule definition with variables
rule plot_histogram:
    input:
        # We can define the input dynamically as output of a different rule
        lambda wildcards: rules.transform_image.output,
    output:
        # File names can be given a variable name which can be referenced in the "shell" command
        histogram_plot=report(
            "../results/histograms/{transformation}_hist.png", category="Histogram"
        ),
    log:
        "../logs/plot_histogram/{transformation}.log",
    conda:
        "../envs/environment.yaml"
    shell:
        "python scripts/plot-histogram.py --image {input} --title astronaut --output {output.histogram_plot}"
