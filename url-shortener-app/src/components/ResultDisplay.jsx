import React from 'react';

export default function ResultDisplay({ result, error, onCopy, copyText, onShare }) {
    if (result) {
        return (
            <div className="alert alert-success mt-4 d-flex justify-content-between align-items-center">
                <span className="text-truncate me-3">{result}</span>
                <div className="d-flex gap-2">
                    <button className="btn btn-outline-secondary btn-sm" onClick={onCopy}>
                        {copyText}
                    </button>
                    <button
                        className="btn btn-outline-primary btn-sm"
                        onClick={onShare}
                        aria-label="Share"
                        title="Share"
                    >
                        Share
                    </button>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="alert alert-danger mt-4">
                {error}
            </div>
        );
    }

    return null;
}
