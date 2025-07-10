import React from 'react';

export default function ExpiryCheckbox({ checked, onChange }) {
  return (
    <div className="mb-3 form-check">
      <input
        type="checkbox"
        className="form-check-input"
        id="setExpiry"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
      />
      <label htmlFor="setExpiry" className="form-check-label">
        Set expiry date
      </label>
    </div>
  );
}
