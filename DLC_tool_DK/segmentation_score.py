"""
scoring metric
D Kim, donniek@bcm.edu
"""

import numpy as np


def dice_coeff(ground_img, predicted_img):
    """
    Input:
        ground_img : array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        predicted_img : array-like, bool
            Any other array of identical size. If not boolean, will be converted.
    Returns:
        jaccard_index : float
            jaccard_index as a float on range [0,1].
            Maximum similarity = 1
            No similarity = 0
            If sum of ground_img and predicted_img = 0, return 0
    """
    ground_img = np.asarray(ground_img).astype(np.bool)
    predicted_img = np.asarray(predicted_img).astype(np.bool)

    if ground_img.shape != predicted_img.shape:
        raise ValueError(
            "Shape mismatch: ground_img and predicted_img must have the same shape.")

    img_sum = ground_img.sum() + predicted_img.sum()
    if img_sum == 0:
        print("sum of two images is equal to 0. Return 0")
        return 0.0

    # Compute Dice coefficient
    intersection = np.logical_and(ground_img, predicted_img)

    return 2. * intersection.sum() / img_sum


def jaccard_index(ground_img, predicted_img):
    """
    Input:
        ground_img : array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        predicted_img : array-like, bool
            Any other array of identical size. If not boolean, will be converted.
    Returns:
        jaccard_index : float
            jaccard_index as a float on range [0,1].
            Maximum similarity = 1
            No similarity = 0
    """
    ground_img = np.asarray(ground_img).astype(np.bool)
    predicted_img = np.asarray(predicted_img).astype(np.bool)

    if ground_img.shape != predicted_img.shape:
        raise ValueError(
            "Shape mismatch: ground_img and predicted_img must have the same shape.")

    intersection = np.logical_and(ground_img, predicted_img)

    denominator = (ground_img.sum() + predicted_img.sum() - intersection.sum())

    if denominator == 0:
        print("denominator is equal to 0. Return 0")
        return 0.0

    return intersection.sum() / denominator


def sensitivity_score(ground_img, predicted_img):
    """
    Input:
        ground_img : array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        predicted_img : array-like, bool
            Any other array of identical size. If not boolean, will be converted.
    Returns:
        sensitivity : float
            sensitivity as a float on range [0,1].
            Maximum similarity = 1
            No similarity = 0
    """
    ground_img = np.asarray(ground_img).astype(np.bool)
    predicted_img = np.asarray(predicted_img).astype(np.bool)

    if ground_img.shape != predicted_img.shape:
        raise ValueError(
            "Shape mismatch: ground_img and predicted_img must have the same shape.")

    intersection = np.logical_and(ground_img, predicted_img)

    return intersection.sum() / ground_img.sum()


def precision_score(ground_img, predicted_img):
    """
    Input:
        ground_img : array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        predicted_img : array-like, bool
            Any other array of identical size. If not boolean, will be converted.
    Returns:
        precision : float
            jaccard_index as a float on range [0,1].
            Maximum similarity = 1
            No similarity = 0
    """
    ground_img = np.asarray(ground_img).astype(np.bool)
    predicted_img = np.asarray(predicted_img).astype(np.bool)

    if ground_img.shape != predicted_img.shape:
        raise ValueError(
            "Shape mismatch: ground_img and predicted_img must have the same shape.")

    intersection = np.logical_and(ground_img, predicted_img)

    return intersection.sum() / predicted_img.sum()


def compute_segmentation_score(ground_img, predicted_img):
    dice = dice_coeff(ground_img, predicted_img)
    jaccard = jaccard_index(ground_img, predicted_img)
    sensitivity = sensitivity_score(ground_img, predicted_img)
    precision = precision_score(ground_img, predicted_img)

    return {'dice_coeff': dice, 'jaccard_index': jaccard, 'sensitivity': sensitivity, 'precision': precision}
