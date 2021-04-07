def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """

    agct = len([i for i in sequence if i.lower() in 'agct'])
    gc = len([i for i in sequence if i.lower() in 'gc'])
    return round((gc / agct) * 100, 2)
